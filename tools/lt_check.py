"""Проверка орфографии, грамматики и пунктуации через публичный API LanguageTool.

Запуск: python tools/lt_check.py путь/к/файлу.md
Текст отправляется на api.languagetool.org — не используйте для закрытых материалов.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.languagetool.org/v2/check"
# Правила, которые на технических текстах дают в основном ложные срабатывания
DISABLED = "WHITESPACE_RULE,UPPERCASE_SENTENCE_START,DASH_RULE"


def paragraphs(md: str) -> list[str]:
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    out = []
    for block in re.split(r"\n\s*\n", md):
        if block.lstrip().startswith(("|", "#")):
            continue
        block = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", block)
        block = re.sub(r"[*_`>]", "", block).strip()
        if len(block.split()) >= 5:
            out.append(block)
    return out


def check(text: str) -> list[dict]:
    data = urllib.parse.urlencode(
        {"text": text, "language": "ru-RU", "disabledRules": DISABLED}
    ).encode()
    with urllib.request.urlopen(urllib.request.Request(API, data=data), timeout=60) as r:
        return json.load(r)["matches"]


def main(path: str) -> None:
    paras = paragraphs(Path(path).read_text(encoding="utf-8"))
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) > 15000:
            chunks.append(cur)
            cur = ""
        cur += p + "\n\n"
    chunks.append(cur)
    print(f"=== {path} ===")
    for chunk in chunks:
        for m in check(chunk):
            ctx = m["context"]
            frag = ctx["text"][ctx["offset"] : ctx["offset"] + ctx["length"]]
            sugg = ", ".join(r["value"] for r in m["replacements"][:3])
            print(f"- [{m['rule']['id']}] «{frag}» → {sugg or '—'}\n    {m['message']}\n    …{ctx['text']}…")
        time.sleep(3)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for a in sys.argv[1:]:
        main(a)
