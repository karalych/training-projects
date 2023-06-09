# Преобразование Гильберта для данных георадара

Самостоятельный проект для научной работы

## Краткое описание

Для интерпретации результатов георадарных исследований часто применяют преобразование Гильберта. Настройки в имеющемся коммерческом софте негибкие, поэтому для научной работы надо было написать скрипт, который бы позволял производить преобразование Гильберта и строить все возможные его выходные параметры - мгновенную амплитуду, мгновенную частоту, мгновенную фазу.

---

## Задачи

1. Загрузить и подготовить данные, полученные в формате csv.
2. Провести преобразование Гильберта.
3. Построить временные разрезы выходных параметров - мгновенной фазы, частоты, амплитуды.
4. Протестировать автоматическую регулировку амплитуд.
5. Построить разрез мгновенной фазы, совпадающий с разрезом в учебнике Старовойтова "Интерпретация георадиолокационных данных" 2008 года.

---

## Данные

Данные в формате csv выгружаются из программы Геоскан 32 - измеренная на объекте "Умревинский острог" в Новосибирской области радарограмма.

## Используемые библиотеки

pandas, matplotlib, numpy, scipy
