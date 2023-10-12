from typing import Iterable
import csv







def aggregation_search(data:Iterable, i_group_by_row: int, i_result_row: int) -> dict:
    """
    Создает словарь, который группирует таблицу по одному столбцу,
    помещая в ключ столбец, по которому происходит группировка,
    а в значения  - другой выбранный столбец
    :param data: список с изначальными данными
    :param i_group_by_row: номер столбца из таблицы (считая с 0), по которому необходимо сгруппировать
    :param i_result_row: номер столбца из таблицы (считая с 0), который помещается в значения


    :return: искомый словарь

     """
    result ={}
    for row in data:
        group_by_row = row[i_group_by_row]
        need_row = row[i_result_row]
        if group_by_row in result:
            if need_row  not in result[group_by_row]:
                result[group_by_row].append(need_row)
        else:
            result.update({group_by_row:[need_row]})

    return result






def make_report(data:Iterable) -> Iterable:
    """
    Создает сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату
    :param data: список с изначальными данными
    :return: список с отчетом

    """
    dict_population = aggregation_search(data,1,0)
    dict_salary = aggregation_search(data,1,5)
    list_report = []
    for key in dict_salary.keys():
        list_report.append(f'Департамент:{key}')
        list_report.append(f'Численность сотрудников: {len(dict_population.get(key))}')
        salaries = list(map(float, dict_salary.get(key)))
        list_report.append(f'"Вилка" зарплат: {min(salaries)}-{max(salaries)}')
        list_report.append(f'Средняя зарплата: {sum(salaries)/len(salaries)}')
    return list_report




def start_menu() -> None:
    """
    Функция сначала распаковывает файл, затем выводится меню, которое состоит из 3-х пунктов:

    1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него
    2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату
    3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2
    Пользователь выбирает пункт меню, вводя соответствующее число.

    """
    data = []
    with open('Corp_Summary.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row[0].split(sep=';'))
        data.pop(0)


    print('Выберете опцию')
    print('1. Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него')
    print('2. Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату')
    print('3. Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2')
    command = int(input())
    if command == 1:
        dict_department = aggregation_search(data,1,2)
        for key in dict_department.keys():
            print(f'Департамент "{key}" включает в себя такие команды:')
            for i in range(len(dict_department.get(key))):
                print(f'{i+1}){dict_department.get(key)[i]}')
    elif command == 2:
        report = make_report(data)
        for s in report:
            print(s)
    elif command == 3:
        print('Введите название файла')
        directory = input()
        report = make_report(data)
        with open(directory+'.csv', "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(report)
    else:
        print('Неверный ввод. Введите число от 1 до 3')



if __name__ == '__main__':
    start_menu()
