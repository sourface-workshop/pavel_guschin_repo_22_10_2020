"""
3. Реализовать базовый класс Worker (работник), в котором
определить атрибуты: name, surname, position (должность), income (доход).

Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения
полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    _income = {'wage': 30000, 'bonus': 5000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def get_full_name(self):
        print(f'{self.position} {self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self.name} имеет доход {sum(self._income.values())}')


a = Position('Ашотик', 'Хачатурян', 'Шаурмен')
a.get_full_name()
a.get_total_income()
