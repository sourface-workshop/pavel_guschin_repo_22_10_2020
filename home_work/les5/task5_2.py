"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
# Использовал файл, созданный из задания 1. Какая разница?


import time

def log(func):
    def wrap(*args):
        t = time.time()
        result = func(*args)
        print(time.time() - t)
        return result
    return wrap

# @log
def string_count(file: str):
    """
    Функция написана забавы ради и больше нафиг нигде не понадобится

    :param file: any text file
    :return: prints
    """

    with open(file, 'r', encoding='utf-8') as f:
        size = sum(1 for _ in f)   # Если требуется СНАЧАЛА подсчет количества строк, то это доп проход по файлу
        print(f'Файл "{f.name}" содержит {size} строк')

    # НЕ ЗНАЮ ПОЧЕМУ, НО ПОСЛЕ ПЕРВОЙ ИТЕРАЦИИ ПО ОБЪЕКТУ F ОН... ОПУСТОШАЕТСЯ?
    # ПОСЛЕ ПЕРВОЙ ИТЕРАЦИИ ПО НЕМУ ОН ПЕРЕСТАЕТ ЧТО-ЛИБО ВОЗВРАЩАТЬ, ПОЭТОМУ ОТКРЫВАЮ ОПЯТЬ:

    with open(file, 'r', encoding='utf-8') as f:
        for _, __ in enumerate(f, 1):
            print(f'Строка №{_} содержит {__.count(" ") + 1} слов и {len(__.rstrip())} символов')


string_count('new_text.txt')
