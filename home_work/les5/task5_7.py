"""
7. Создать (не программно) текстовый файл, в котором каждая строка
должна содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""


import json


companies = {}

with open('companies.txt', 'r', encoding='utf-8') as comp:
    for itm in comp:
        data = itm.split()  # Получаем список из строки
        companies[data[0]] = int(data[2]) - int(data[3])    # Добавляем инфу в словарь. Ключ - имя, прибыль - арифметика
average = {'average_profit': sum(filter(lambda x: x >= 0, companies.values())) / len(companies)}    # Из основного
                                        # словаря фильтруем отрицательные значения, суммируем, делим на количество фирм

total = [companies, average]            # Итоговый список со словарями

with open('companies_info.json', 'w', encoding='utf-8') as f:
    json.dump(total, f)
