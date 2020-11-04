"""
3. Реализовать функцию my_func(), которая принимает
три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


# Решил заморочиться - аргументов может быть сколько угодно,
# для суммирования можно выбирать любое количество аргов,
# можно выбирать как наибольшие, так и наименьшие аргументы

# Описание функций есть в toolbox. Здесь убрал для экономии пространства

def my_minimax(*args, maximal=True, count=1, duplicated=True) -> list:
    if not duplicated:
        args = frozenset(args)
    order = sorted(args, reverse=maximal)
    result = []

    for i in range(count):
        if order:
            result.append(order.pop(0))
    return result


def my_sum(*args: float) -> float:
    result = 0

    for arg in args:
        result += arg
    return result


def my_func(*args, count=2):
    a = my_minimax(*args, count=count)
    result = my_sum(*a)
    return result


print(my_func(7, 2, 6, 4, 9))
