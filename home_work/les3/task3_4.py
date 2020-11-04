"""
4. Программа принимает действительное положительное число x
и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

# Почему только отрицательные числа? Пусть любые принимает и считает соответственно

def my_pow(number: float, power: int) -> float:
    """
    Function returns number raised to the power

    :param number: any int or float number
    :param power: any int number (pos or neg)
    :return: number to power
    """

    # Простая реализация
    # try:
    #     return number ** power
    # except TypeError as te:
    #     print('Аргументами могут быть только числа!')

    result = 1
    try:
        if power:
            for i in range(abs(power)):
                result *= number
        else: return result
        return result if power > 0 else 1 / result
    except TypeError as te:
        print('Аргументами могут быть только числа!')


print(my_pow(2, -3))