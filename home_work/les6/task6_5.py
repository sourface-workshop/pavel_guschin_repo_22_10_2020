"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


# Не уверен, что правильно понял ТЗ. Как-то все слишком просто...


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Чертим карандашом')


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Выделяем маркером')


pen = Pen('Синяя ручка')
pncl = Pencil('Карандаш ТМ')
h = Handle('Зеленый маркер')
