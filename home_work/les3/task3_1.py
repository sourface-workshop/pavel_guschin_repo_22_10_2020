"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div(a: float, b: float) -> float:
    """
    Function divides param a by param b

    :param a: any int or float number
    :param b: any int or float number except zero
    :return: division result as float number
    """
    try:
        if a: return a / b
        else: return 0
    except TypeError as te:
        print('Можно вводить только 2 числа!\n')
    except ZeroDivisionError as zde:
        print('Нельзя делить на ноль!\n')


a = my_div(10, 5)
print(a)