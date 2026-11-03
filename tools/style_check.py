"""Проверка стиля русских конспектов в Markdown.

Правила адаптированы из Humanizer RU (https://github.com/comol/Humanizer_RU, MIT):
канцелярит, пустые зачины и выводы, раздувание значимости, формула «не просто X, а Y»,
ритм предложений. Добавлены свои маркеры «машинного» текста.

Запуск: python tools/style_check.py путь/к/файлу.md [ещё файлы]
"""
import re
import statistics
import sys
from pathlib import Path

RULES = {
    "high": {
        "пустой зачин": r"в\s+современном\s+мире|в\s+наше\s+время|не\s+секрет,?\s+что|в\s+эпоху\s+\w+",
        "анонс вместо дела": r"вот\s+что\s+(?:нужно|важно|стоит)\s+знать|в\s+(?:этой|данной)\s+статье|итак,\s+начн|разбер[её]м\s+по\s+порядку|^\s*ниже\s+[—-]",
        "пустой переход": r"(?:важно|стоит|следует|необходимо|нужно)\s+(?:отметить|подчеркнуть|заметить)|нельзя\s+не\s+(?:отметить|упомянуть)",
        "раздувание значимости": r"игра\w*\s+(?:важную|ключевую|решающую|огромную)\s+роль|трудно\s+переоценить|неотъемлем\w+|краеугольн\w+|поворотн\w+\s+(?:момент|пункт)|смен\w+\s+парадигм",
        "пустой вывод": r"подводя\s+итог|в\s+заключение|резюмируя|в\s+целом\s+можно\s+сказать|открыва\w+\s+новые\s+(?:горизонты|возможности)",
        "размытая ссылка": r"по\s+мнению\s+экспертов|эксперты\s+(?:считают|отмечают)|исследования\s+показывают|общеизвестно",
        "«не просто X, а Y»": r"не\s+просто\s+[^.!?\n]{1,80}?,\s*(?:а|но)\s|это\s+не\s+(?:просто|только)\s+[^.!?\n]{1,40}[,—–-]\s*(?:а|но|это)\s",
        "псевдоглубина": r"на\s+самом\s+деле|секрет\s+в\s+том|главная\s+ошибка|если\s+копнуть",
        "машинная рамка": r"^#+\s*коротко\s*$|это\s+и\s+есть\b|главн\w+\s+мысль|ключев\w+\s+(?:вывод|идея|мысль)|простой\s+расч[её]т|важно\s+понимать",
    },
    "low": {
        "канцелярский глагол": r"осуществл\w+|принима\w+\s+участие|име(?:ет|ют)\s+место\b|представляется\s+возможным",
        "предложный штамп": r"в\s+целях\b|посредством\b|в\s+рамках\b|в\s+связи\s+с\s+тем|в\s+силу\s+того|путём\s+\w+ния",
        "«данный»": r"\bданн(?:ый|ая|ое|ого|ому|ую|ой|ом)\b",
        "раздутая связка": r"представля\w+\s+собой|выступа\w+\s+в\s+(?:роли|качестве)|явля\w+\s+(?:важн|ключев|одним\s+из|одной\s+из|основ|главн)",
        "рекламная оценка": r"уникальн\w+|революционн\w+|инновационн\w+|мощн\w+\s+(?:инструмент|решени)|широк\w+\s+спектр|лучш\w+\s+практик",
        "калька": r"в\s+конечном\s+итоге|на\s+(?:ежедневной|регулярной)\s+основе|делает\s+возможным|адресова\w+\s+(?:проблем|вопрос)",
        "анонс-приглашение": r"давайте\s+(?:разбер|рассмотр|посмотр|погруз)\w*",
        "вводный вывод": r"(?:^|[.!?]\s+)таким\s+образом,",
        "афоризм": r"[^.!?\n]{2,40}\s—\s(?:это\s+)?(?:нов\w+\s+)?(?:валюта|нефть|суперсила)\b",
    },
    "note": {
        "заполнитель": r"\bпо\s+сути\b|по\s+большому\s+сч[её]ту|в\s+принципе,|так\s+или\s+иначе,|в\s+любом\s+случае,",
        "усилитель": r"\b(?:очень|крайне|действительно|абсолютно|безусловно|невероятно|поистине|несомненно|чрезвычайно)\b",
    },
}
WEIGHT = {"high": 3, "low": 1, "note": 0.3}


def prose(md: str) -> str:
    """Убирает код, таблицы, ссылки и разметку, оставляя связный текст."""
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    lines = [l for l in md.splitlines() if not l.lstrip().startswith("|")]
    text = "\n".join(lines)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`>#]", "", text)
    return text


def sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?…])\s+|\n{2,}", text)
    return [p.strip() for p in parts if len(p.split()) >= 2]


def check(path: Path) -> None:
    raw = path.read_text(encoding="utf-8")
    text = prose(raw)
    words = len(re.findall(r"\w+", text))
    hits = []
    for level, rules in RULES.items():
        for name, rx in rules.items():
            for m in re.finditer(rx, text, flags=re.I | re.M):
                line = text[: m.start()].count("\n") + 1
                hits.append((level, name, m.group(0).strip(), line))

    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    long_s = [s for s in sents if len(s.split()) > 30]
    cv = statistics.pstdev(lens) / statistics.mean(lens) if len(lens) > 1 else 0
    dashes = len(re.findall(r"\s—\s", text))
    bold = len(re.findall(r"\*\*[^*]+\*\*", raw))
    bullets = len(re.findall(r"^\s*(?:[-*]|\d+\.)\s", raw, flags=re.M))
    nonempty = len([l for l in raw.splitlines() if l.strip()])
    hrs = len(re.findall(r"^---\s*$", raw, flags=re.M))

    penalty = sum(WEIGHT[h[0]] for h in hits)
    penalty += max(0, (dashes / max(words, 1) * 100 - 2.5) * 4)
    penalty += max(0, (0.45 - cv) / 0.45 * 15)
    penalty += 2 * len(long_s) + 2 * hrs
    penalty += max(0, (bold - words / 200 - 1))
    score = max(0, round(100 - penalty))

    print(f"\n=== {path}  ({words} слов, {len(sents)} предложений) ===")
    for level, name, frag, line in sorted(hits, key=lambda h: h[3]):
        print(f"  [{level:4}] стр.~{line:<4} {name}: «{frag}»")
    print(f"  ритм: средняя длина {statistics.mean(lens):.1f} слова, CV={cv:.2f} (норма ≥0.45)")
    print(f"  длинных предложений (>30 слов): {len(long_s)}")
    print(f"  тире на 100 слов: {dashes / max(words, 1) * 100:.1f} (норма ≤2.5)")
    print(f"  жирный шрифт: {bold}; пунктов списков: {bullets} из {nonempty} строк; разделителей ---: {hrs}")
    print(f"  ОЦЕНКА: {score}/100  ({'чисто' if score >= 85 else 'точечная правка' if score >= 60 else 'переписать'})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for arg in sys.argv[1:]:
        check(Path(arg))
