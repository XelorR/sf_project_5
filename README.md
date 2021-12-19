﻿# SF Проект номер 5: Компьютер говорит НЕТ

Проект включает в себя [состязание на Кеггле](https://www.kaggle.com/c/sf-scoring)

> Если хотите перейти сразу к делу, вот финальный ноутбук: [pp_baseline_short.ipynb](pp_baseline_short.ipynb)

## История исследования и описание ноутбуков в репозитории

В хронологическом порядке. Более детальные подробности - в самих ноутбуках.

### kaggle score 0.04067, [Credit_scoring.ipynb](Credit_scoring.ipynb)

Ноутбук Артура, основан на бейзлайне. Ознакомившись с ним, я сделал ряд выводов, которые мне помогли в дальнейшем

### [overview_pp_skillfactory_tasks.ipynb](overview_pp_skillfactory_tasks.ipynb)

В этом ноутбуке я решал задачи курса, в процессе улучшил некоторые из своих [функций для визуализации данных](data_viz_functions.py)

### kaggle score 0.06177, [overview_kaggle_pp_first_try.ipynb](overview_kaggle_pp_first_try.ipynb)

Здесь я впервые ознакомился с версией датасета с кеггла и начал препроцессинг

### kaggle score 0.06658, [pp_scoring_from_scratch.ipynb](pp_scoring_from_scratch.ipynb)

Версия предыдущего, переписанная с нуля чтоб не путаться, занимался перебором моделей

### kaggle score 0.33933, [pp_tuned_baseline.ipynb](pp_tuned_baseline.ipynb)

Второй бейзлайн, взятый с кеггла, хороший препроцессинг и хорошо подобранные параметры линейной регрессии. Исправив несколько ошибок, увеличил рейтинг, также играл в разные можели, проверял что работает, а что нет

### kaggle score **0.34004**, [pp_baseline_short.ipynb](pp_baseline_short.ipynb)

**Финальный**. Переписанный с нуля предыдущий. Изучил фреймворк [Optuna](https://optuna.org/) для оптимизации гипперпараметров, выбрал модель, подобрал гипперпараметры к модели, попробовал различные метрики для оптимизации, сравнил множество моделей, выбрал лучшую.

### [pp_pycaret.ipynb](pp_pycaret.ipynb)

Прочитал о чудесном фреймворке [PyCaret](https://pycaret.org/), очень хотел опробовать его на нашей задаче, но, к сожалению, в виду ограниченности во времени пришлось эту идею отложить. Может как-нибудь вернусь

## Кратко основные вынесенные мысли

- слишком много всего, что можно попробовать, нужно выделять главное и игнорировать второстепенное
- не всегда решает самая мощная модель
- хороший результат на валидации ещё не означает хорошего результата не тесте
- нужно глубже уйти во фреймворки для оптимизации. Оптимизировать оказывается можно не только гипперпараметры, но и препроцессинг и вообще что угодно
- хоть я этого и нк реализовал, теоретически никто не мешает засунуть в **Optuna** сколько угодно моделей и какую угодно логику. Можно пойти дальше и составлять комбинации моделей, настроив выход или ошибку одной на вход другой, например. Огромный простор для оптимизационного творчества
- минимум по кроссвалидированному roc_auc эффективнее болется с переоучением, чем среднее или медиана
- нужно больше соревнований, мне понравилось :)
