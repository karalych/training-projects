# Выбор места для скважины

Третий учебный проект по машинному обучению: регрессия и анализ возможной прибыли с бустрапом

## Краткое описание

Нужно решить, где бурить новую скважину.

Есть пробы нефти в трёх регионах: в каждом 100 000 скважин, где измерили качество нефти и объём её запасов. 

Надо построить модель машинного обучения, которая поможет определить регион, где добыча принесёт наибольшую прибыль. При этом, проанализировать возможную прибыль и риски техникой *Bootstrap.*

Шаги для выбора локации:

- В избранном регионе ищут месторождения, для каждого определяют значения признаков;
- Строят модель и оценивают объём запасов;
- Выбирают месторождения с самым высокими оценками значений. Количество месторождений зависит от бюджета компании и стоимости разработки одной скважины;
- Прибыль равна суммарной прибыли отобранных месторождений.
---

## Задачи

**Условия задачи:**
 * Для обучения модели подходит только линейная регрессия (остальные — недостаточно предсказуемые).
 * При разведке региона исследуют 500 точек, из которых с помощью машинного обучения выбирают 200 лучших для разработки.
 * Бюджет на разработку скважин в регионе — 10 млрд рублей.
 * При нынешних ценах один баррель сырья приносит 450 рублей дохода. Доход с каждой единицы продукта составляет 450 тыс. рублей, поскольку объём указан в тысячах баррелей.
 * После оценки рисков нужно оставить лишь те регионы, в которых вероятность убытков меньше 2.5%. Среди них выбирают регион с наибольшей средней прибылью.
 * Данные синтетические: детали контрактов и характеристики месторождений не разглашаются.

**План работы**

1. Загрузить и подготовить данные.
2. Обучить и проверить модель для каждого региона:
    - Разбить данные на обучающую и валидационную выборки в соотношении 75:25.
    - Обучить модель и сделать предсказания на валидационной выборке.
    - Сохранить предсказания и правильные ответы на валидационной выборке.
    - Вывести средний запас предсказанного сырья и RMSE модели.
    - Проанализировать результаты.
3. Подготовиться к расчёту прибыли:
    - Все ключевые значения для расчётов сохранить в отдельных переменных.
    - Рассчитайть достаточный объём сырья для безубыточной разработки новой скважины. Сравнить полученный объём сырья со средним запасом в каждом регионе. 
    - Сделать выводы по этапу подготовки расчёта прибыли.
4. Написать функцию для расчёта прибыли по выбранным скважинам и предсказаниям модели:
    - Выберать скважины с максимальными значениями предсказаний. 
    - Просуммировать целевое значение объёма сырья, соответствующее этим предсказаниям.
    - Рассчитать прибыль для полученного объёма сырья.
5. Посчитайть риски и прибыль для каждого региона:
    - Применить технику Bootstrap с 1000 выборок, чтобы найти распределение прибыли.
    - Найти среднюю прибыль, 95%-й доверительный интервал и риск убытков. Убыток — это отрицательная прибыль.
    - Сделать выводы: предложить регион для разработки скважин и обосновать выбор.

---

## Данные

Данные геологоразведки трёх регионов находятся в файлах: 
 - `geo_data_0.csv`. 
 - `geo_data_1.csv`. 
 - `geo_data_2.csv`.

Структура файла:

 * `id` — уникальный идентификатор скважины;
 * `f0`, `f1`, `f2` — три признака точек (неважно, что они означают, но сами признаки значимы);
 * `product` — объём запасов в скважине (тыс. баррелей).

---

## Используемые библиотеки

pandas, matplotlib, sklearn, numpy
