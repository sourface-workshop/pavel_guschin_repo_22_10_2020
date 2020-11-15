"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Let's move! {self.name} is going ahead!")

    def stop(self):
        print(f'{self.name} has stopped')

    def turn(self, direction: str):
        print(f'{self.name} turned {direction}')

    def show_speed(self):
        print(f'Speed of {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(color, name, False)
        self.speed = speed
        self.__max_spd = 60

    def show_speed(self):
        print(f'Speed: {self.speed}' if self.speed <= self.__max_spd else f'Speed {self.speed} is too high!')

t = TownCar(50, 'Red', 'Hyundai')


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(color, name, False)
        self.speed = speed
        self.__max_spd = 40

    def show_speed(self):
        print(f'Speed: {self.speed}' if self.speed <= self.__max_spd else f'Speed {self.speed} is too high!')


w = WorkCar(50, 'yellow', 'Tractor')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(color, name, False)
        self.speed = speed
        self.__max_spd = float('inf')

    def show_speed(self):
        print(f'Speed: {self.speed}' if self.speed <= self.__max_spd else f'Speed {self.speed} is too high!')


s = SportCar(100, 'Black', 'Ferrari')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(color, name, True)
        self.speed = speed
        self.__max_spd = float('inf')

    def show_speed(self):
        print(f'Speed: {self.speed}' if self.speed <= self.__max_spd else f'Speed {self.speed} is too high!')


p = PoliceCar(120, 'Blue', 'GMC')

print(1)