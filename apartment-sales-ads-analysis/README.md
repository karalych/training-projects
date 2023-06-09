# Исследование объявлений о продаже квартир

Второй учебный проект, сконцентрированный на предобработке и анализе данных

## Краткое описание

Цель работы: понять, от чего зависит рыночная стоимость объектов недвижимости.

---

## Задачи

План работ:
1. Открыть и изучить информацию о данных.
2. Провести предобработку данных:
    - изучить и заполнить, где это возможно, пропуски;
    - изучить и исправить типы данных;
    - исправить дубликаты;
    - удалить редкие и выбивающиеся значения.
3. Добавить в таблицу новые столбцы со следующими параметрами:
    - цена одного квадратного метра;
    - день недели публикации объявления (0 — понедельник, 1 — вторник и так далее);
    - месяц публикации объявления;
    - год публикации объявления;
    - тип этажа квартиры (значения — «первый», «последний», «другой»);
    - расстояние до центра города в километрах (до целых значений).
4. Провести исследовательский анализ данных:
    - изучить распределения некоторых параметров;
    - изучить, как быстро продавались квартиры;
    - посмотреть, какие факторы и как влияют на общую стоимость квратиры;
    - посчитать среднюю цену одного квадратного метра в 10 населённых пунктах с наибольшим числом объявлений и выделить населённые пункты с самой высокой и низкой стоимостью квадратного метра;
    - вычислить среднюю цену каждого километра от центра города в Санкт-Петербурге.
5. Написать общий вывод.

---

## Данные

В нашем распоряжении данные сервиса Яндекс.Недвижимость — архив объявлений о продаже квартир в Санкт-Петербурге и соседних населённых пунктов за несколько лет.

По каждой квартире на продажу доступны два вида данных. Первые вписаны пользователем, вторые — получены автоматически на основе картографических данных. Например, расстояние до центра, аэропорта, ближайшего парка и водоёма. 

* `airports_nearest` — расстояние до ближайшего аэропорта в метрах (м)
* `balcony` — число балконов
* `ceiling_height — высота потолков (м)
* `cityCenters_nearest — расстояние до центра города (м)
* `days_exposition — сколько дней было размещено объявление (от публикации до снятия)
* `first_day_exposition` — дата публикации
* `floor` — этаж
* `floors_total` — всего этажей в доме
* `is_apartment` — апартаменты (булев тип)
* `kitchen_area` — площадь кухни в квадратных метрах (м²)
* `last_price` — цена на момент снятия с публикации
* `living_area` — жилая площадь в квадратных метрах (м²)
* `locality_name` — название населённого пункта
* `open_plan` — свободная планировка (булев тип)
* `parks_around3000` — число парков в радиусе 3 км
* `parks_nearest` — расстояние до ближайшего парка (м)
* `ponds_around3000` — число водоёмов в радиусе 3 км
* `ponds_nearest` — расстояние до ближайшего водоёма (м)
* `rooms` — число комнат
* `studio` — квартира-студия (булев тип)
* `total_area` — общая площадь квартиры в квадратных метрах (м²)
* `total_images` — число фотографий квартиры в объявлении

---

## Используемые библиотеки

pandas, matplotlib
