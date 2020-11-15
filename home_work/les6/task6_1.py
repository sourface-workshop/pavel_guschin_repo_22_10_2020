"""
1. Создать класс TrafficLight (светофор) и определить у него
один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""


from time import sleep


class TrafficLight:
    __color = [('красный', 7), ('желтый', 2), ('зеленый', 10), 0]

    def running(self):                  # Следующие три строки только для наглядности и укорочения дальнейшей писанины
        mode = self.__color[-1]         # Это переключение состояний светофора
        color = self.__color[mode][0]   # Это цвет (берется по индексу из списка)
        sec = self.__color[mode][1]     # Это количество секунд
        for i in range(sec):
            print(f'{color}: {sec}')    # Для наглядности принтуем, что цвет сейчас такой-то и остаток секунд
            sec -= 1
            sleep(1.0)
        if self.__color[3] < 2:         # Смена режима или сброс режима в 0, если все цвета прошли
            self.__color[3] += 1
        else:
            self.__color[3] = 0


device = TrafficLight()
device.running()
