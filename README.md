Django Tree Menu 

Этот проект реализует древовидное меню в Django, соответствующее следующим требованиям:

Условия задания

1. Меню реализовано через `template tag`.
2. Все, что над выделенным пунктом — развернуто. Первый уровень вложенности под активным пунктом тоже развернут.
3. Структура меню хранится в базе данных.
4. Меню редактируется через стандартную админку Django.
5. Активный пункт определяется на основе текущего URL страницы.
6. На одной странице может быть несколько меню — они определяются по названию.
7. Переход по клику осуществляется на заданный URL — как абсолютный, так и через `named url`.
8. Для отрисовки каждого меню выполняется ровно 1 SQL-запрос.
