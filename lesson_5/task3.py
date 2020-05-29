"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников. """


def cut_spaces(txt: str):  # Убирает лишние пробелы в строке
    while txt.find('  ') != -1:
        txt = txt.replace('  ', ' ')
    return txt.strip()


def emp_to_list(txt: str):
    txt = cut_spaces(txt)
    if len(txt) < 3 or txt.count(' ') != 1:
        return False
    surname = txt[:txt.find(' ')]
    try:
        salary = float(txt[txt.find(' ')+1:])
    except ValueError:
        return False
    if salary % 1 == 0:  # Бесят нули после точки, да и памяти меньше занимает
        salary = int(salary)
    return [surname, salary]


total_salary = 0
i = 0  # Счетчик корректных строк
j = 1  # Счетчик общего числа строк
error_rows = ''
with open('task3/task3.txt', mode='r', encoding='utf-8') as r_file:
    for cur_line in r_file:
        cur_emp = emp_to_list(cur_line)
        if cur_emp:
            if cur_emp[1] < 20000:
                print(cur_emp[0], ' ', cur_emp[1])
            total_salary += cur_emp[1]
            i += 1
        else:
            error_rows += str(j) + ', '
        j += 1

print('\nСредняя зарплата: ', round(total_salary / i, 2))
if error_rows:
    print('\nВнимание! Строка', error_rows[:-2], 'содержит ошибки. Проверьте корректность данных в файле.')
