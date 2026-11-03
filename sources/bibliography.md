# Список источников

Источники сгруппированы по темам. Для каждого указано, зачем он нужен. Отметка ★ — прочитать в первую очередь.

## Истоки и принципы

| Источник | Зачем |
|---|---|
| Conway M. E. *How Do Committees Invent?* Datamation, 1968 | Закон Конвея: архитектура повторяет структуру организации |
| Parnas D. L. *On the Criteria To Be Used in Decomposing Systems into Modules.* CACM 15(12), 1972 | Сокрытие информации, критерии разбиения на модули |
| McIlroy M. D. et al. *UNIX Time-Sharing System: Foreword.* Bell System Technical Journal, 1978 | Философия Unix |
| Birrell A., Nelson B. *Implementing Remote Procedure Calls.* ACM TOCS, 1984 | RPC |
| Deutsch P. *The Eight Fallacies of Distributed Computing*, 1994–1997 | Почему сеть — не вызов функции |
| Fowler M. *Patterns of Enterprise Application Architecture.* 2002 | «Первый закон распределённых объектов» |
| Fielding R. *Architectural Styles and the Design of Network-based Software Architectures.* PhD thesis, UC Irvine, 2000 | REST |
| Evans E. *Domain-Driven Design.* Addison-Wesley, 2003 | Ограниченный контекст — граница сервиса |
| Nygard M. *Release It!* Pragmatic Bookshelf, 2007 (2-е изд. — 2018) | Circuit breaker, bulkhead, таймауты |
| Wiggins A. *The Twelve-Factor App.* https://12factor.net, 2011 | Правила облачных приложений |

## Становление микросервисов

| Источник | Зачем |
|---|---|
| ★ Lewis J., Fowler M. *Microservices.* https://martinfowler.com/articles/microservices.html, 2014 | Каноническое определение, 9 характеристик, история термина |
| ★ Newman S. *Building Microservices.* O'Reilly, 2015; 2-е изд. 2021 | Основной учебник |
| Newman S. *Monolith to Microservices.* O'Reilly, 2019 | Миграция, паттерн «душитель» |
| Richardson C. *Microservices Patterns.* Manning, 2018; https://microservices.io | Каталог паттернов: саги, outbox, CQRS |
| Fowler M. *MonolithFirst*, *Microservice Premium*, 2015 (martinfowler.com) | Когда микросервисы не нужны |
| Fowler M. *StranglerFigApplication*, 2004 (martinfowler.com) | Постепенная миграция |
| Gray J. *A Conversation with Werner Vogels.* ACM Queue 4(4), 2006 | Опыт Amazon, «you build it, you run it» |
| Izrailevsky Y. *Completing the Netflix Cloud Migration.* Netflix, 2016 | Миграция Netflix в облако |
| Skelton M., Pais M. *Team Topologies.* IT Revolution, 2019 | Команды под сервисную архитектуру |

## Отрезвление и альтернативы

| Источник | Зачем |
|---|---|
| Noonan A. *Goodbye Microservices.* Segment Engineering Blog, 2018 | Возврат к монолиту |
| Westeinde K. *Deconstructing the Monolith.* Shopify Engineering, 2019 | Модульный монолит |
| Gluck A. *Introducing Domain-Oriented Microservice Architecture.* Uber Engineering, 2020 | Укрупнение сервисов в домены |
| Ghemawat S. et al. *Towards Modern Development of Cloud Applications.* HotOS, 2023 | Логический монолит, разделение кода и развёртывания |
| Kolny M. *Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%.* Prime Video Tech, 2023 | Отказ от распределённой схемы ради стоимости |

## Производительность и данные

| Источник | Зачем |
|---|---|
| ★ Dean J., Barroso L. A. *The Tail at Scale.* CACM 56(2), 2013 | Хвостовая задержка и веерные запросы |
| Kanev S. et al. *Profiling a Warehouse-Scale Computer.* ISCA, 2015 | «Налог дата-центра» — около 30% циклов |
| Sigelman B. et al. *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure.* Google Technical Report, 2010 | Распределённая трассировка |
| Garcia-Molina H., Salem K. *Sagas.* SIGMOD, 1987 | Длинные транзакции без блокировок |
| Gilbert S., Lynch N. *Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services.* SIGACT News, 2002 | Теорема CAP |
| Verma A. et al. *Large-scale cluster management at Google with Borg.* EuroSys, 2015 | Предшественник Kubernetes |

## Эталонные приложения и трассы (понадобятся для стенда)

| Источник | Зачем |
|---|---|
| ★ Gan Y. et al. *An Open-Source Benchmark Suite for Microservices and Their Hardware-Software Implications for Cloud & Edge Systems* (DeathStarBench). ASPLOS, 2019 | Social Network, Hotel Reservation и др. |
| Zhou X. et al. *Fault Analysis and Debugging of Microservice Systems: Industrial Survey, Benchmark System, and Empirical Study* (TrainTicket). IEEE TSE, 2018 | Большое эталонное приложение |
| Luo S. et al. *Characterizing Microservice Dependency and Performance: Alibaba Trace Analysis.* SoCC, 2021 | Реальные графы вызовов и профили нагрузки |
| Google *Online Boutique*: https://github.com/GoogleCloudPlatform/microservices-demo | Небольшое демо (11 сервисов) — кандидат для стенда |

## Работы по теме НИР (из постановки задачи)

| Источник | Зачем |
|---|---|
| ★ Wang Z. et al. *Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices.* NSDI, 2024. https://www.usenix.org/conference/nsdi24/presentation/wang-zibo | Основной метод |
| Saxena et al. *Towards Performance Robustness for Microservices* (Galileo). NSDI, 2026. https://www.usenix.org/conference/nsdi26/presentation/saxena | Устойчивость к возмущениям |
| Serracanta et al. *On the Stability of the Kubernetes Horizontal Autoscaler Control Loop.* IEEE Access, 2025. https://doi.org/10.1109/ACCESS.2025.3526751 | Формальная модель устойчивости HPA |
| Ahmad et al. *Towards Resource Efficient Reactive and Proactive Auto Scaling for Microservice Architectures.* JSS, 2025. https://doi.org/10.1016/j.jss.2025.112390 | Базовый метод сравнения, сценарии нагрузки |
| Ho et al. *GraphPilot.* UCC, 2025. https://doi.org/10.1145/3773274.3774260 | Колебания при масштабировании связанных сервисов |

## Документация

- Kubernetes: *Horizontal Pod Autoscaling* — https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/
- Kubernetes: *Resource Management for Pods and Containers* — https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Linux kernel: *CFS Bandwidth Control* — https://docs.kernel.org/scheduler/sched-bwc.html
