"""
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


with open('employers.txt', 'r', encoding='utf-8') as f:
    try:
        emps = {_.split()[0]: float(_.split()[1]) for _ in f}
        emps_lowrate = [name for name, rate in emps.items() if rate < 20000]   # <- По-моему, так проще
        # emps_lowrate = [itm[0] for itm in filter(lambda item: int(item[1]) < 20000, emps.items())]
        average_rate = sum(value for value in emps.values()) / len(emps)
        print(f'Сотрудники с окладом ниже 20к: {", ".join(emps_lowrate)}')
        print(f'Средний доход всех сотрудников: {average_rate}')
    except ValueError:
        print('Данные о зарплате введены некорректно')
