"""sum()
map()
min()
max()
enumerate()
zip()
"""


def my_sum(*args: float) -> float:
    """
    Returns sum of passed args

    :param args: int or float numbers
    :return: sum of numbers
    """
    result = 0

    for arg in args:
        result += arg

    return result


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
        print('Можно вводить только цифры!\n')
    except ZeroDivisionError as zde:
        print('Нельзя делить на ноль!\n')


def my_minimax(*args, maximal=True, count=1, duplicated=True) -> list:
    """
    Function returns a list of the specified count (1 by default)
    of max (by default) or min numbers from the passed args.

    If duplicated = True (by default), the same numbers will be included.

    If the amount of args is less than the specified count,
    the number of elements in the returned list will be equal
    to the amount of args.

    :param args: any int or float numbers
    :return: list of int or float numbers
    """

    if not duplicated:
        args = frozenset(args)

    order = sorted(args, reverse=maximal)

    result = []

    for i in range(count):
        if order:
            result.append(order.pop(0))

    return result


# print(my_minimax(1, 2, 3, 4, 4, 3, 3, 3, 5, count=2))


def my_pow(number: float, power: int) -> float:
    """
    Function returns number raised to the power

    :param number: any int or float number
    :param power: any int number (pos or neg)
    :return: number to power
    """

    # try:
    #     return number ** power
    # except TypeError as te:
    #     print('Аргументами могут быть только числа!')

    result = 1
    try:
        if power:
            for i in range(abs(power)):
                result *= number
            if power < 0:
                result = 1 / result
        else: result = 0
        return result
    except TypeError as te:
        print('Аргументами могут быть только числа!')


# print(my_pow(2, 3.5))
# print(pow(2, 3.5))

def isint(number):
    """
    Takes a number whose class you want to determine

    :param number: any int or float number
    :return: class of passed number
    """
    try:
        if int(number) / float(number) == 1.0:
            return int
        else:
            return float
    except ValueError as ve:
        pass


def uppercase(string: str, each=False) -> str:
    for i in range(len(string)):
        if string[i].isalpha() and not string[i - 1:i].isalpha():
            string = string[:i] + string[i].upper() + string[i + 1:]
            if not each: break
    return string

# print(uppercase('2', each=True))