print('Задача №1. Оболочка этого ДЗ...')
print('Задача №2. Пользователь вводит время в секундах...')
print('Задача №3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn')
print('Задача №4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе...')
print('Задача №5. Запросите у пользователя значения выручки и издержек фирмы...')
print('Задача №6. Спортсмен занимается ежедневными пробежками...')
print('\n-------------------------------------------------------------------------------------------------\n')

while True:
    task_number = input('Введите номер задачи от 2 до 6 (для выхода введите 00)\n')
    if task_number == '00':
        break
    if task_number.isdigit():
        task_number = int(task_number)
        if task_number < 2 or task_number > 6:
            continue
    else:
        continue

    print('ЗАДАЧА №', task_number)
    if task_number == 2:
        while True:
            seconds = input('Введите время в секундах (для выхода введите 00)\n')
            if seconds == '00':
                break
            if not seconds.isdigit():
                print('Ошибка ввода')
                continue
            seconds = int(seconds)
            entered_seconds = seconds
            hours = seconds // 3600
            seconds = seconds % 3600
            minutes = seconds // 60
            seconds = seconds % 60
            print('{} сек = {:0=2}:{:0=2}:{:0=2}'.format(entered_seconds, hours, minutes, seconds))
            seconds = ''

    elif task_number == 3:
        while True:
            n_number = input('Введите число n (для выхода введите 00)\n')
            if n_number == '00':
                break
            if not n_number.isdigit():
                print('Ошибка ввода')
                continue
            n_number = int(n_number)
            if n_number < 0:
                print('Принцип решения для отрицательных чисел не задан, попробуйте положительные\n')
                n_number = ''
                continue
            if 0 <= n_number <= 9:
                print('Результат равен', n_number * 123)
            else:
                n_number_2 = str(n_number) + str(n_number)
                n_number_3 = n_number_2 + str(n_number)
                print('Результат равен', n_number + int(n_number_2) + int(n_number_3))
            n_number = ''

    elif task_number == 4:
        while True:
            user_num = input('Введите целое положительное число (для выхода введите 00)\n')
            if user_num == '00':
                break
            if not user_num.isdigit():
                print('Ошибка ввода')
                continue

            user_num = int(user_num)
            most_big_num = 0

            while user_num >= 10:
                rem_div = user_num % 10  # Остаток от деления
                user_num = user_num // 10  # Целочисленное деление
                if rem_div > most_big_num:
                    most_big_num = rem_div
            if user_num > most_big_num:
                most_big_num = user_num
            print('Самая большая цифра: ', most_big_num)
            user_num = ''

    elif task_number == 5:
        while True:
            revenue = input('Введите значение выручки фирмы (для выхода введите 00)\n')
            if revenue == '00':
                break
            costs = input('Введите значение издержек фирмы (для выхода введите 00)\n')
            if costs == '00':
                break
            if not(revenue.isdigit() and costs.isdigit()):
                print('Ошибка ввода\n')
                continue
            revenue = int(revenue)
            costs = int(costs)
            if costs > revenue:
                print('Фирма работает с убытками')
            elif costs == revenue:
                print('Фирма работает в ноль')
            else:
                profitability = round(((revenue - costs) / revenue) * 100, 2)
                print('Фирма работает с прибылью, рентабильность: {}%'.format(profitability))

                while True:
                    employees_numb = input('Введите количество сотрудников\n')
                    if employees_numb.isdigit():
                        employees_numb = int(employees_numb)
                        if employees_numb <= 0:
                            print('Количество сотрудников должно быть больше 0')
                            continue
                        else:
                            break
                print('Прибыль на одного сотрудника:', (revenue - costs) / employees_numb)
            revenue = ''
            costs = ''
            print('\n###########Задача завершена###########\n')

    elif task_number == 6:
        while True:
            a = input('Введите значение дистанции первого дня (a) (для выхода введите 00)\n')
            if a == '00':
                break
            b = input('Введите целевое значение дистанции (b) (для выхода введите 00)\n')
            if b == '00':
                break
            if not(a.isdigit() and b.isdigit()):
                continue
            a = int(a)
            b = int(b)
            if a > b or a <= 0:
                print('Ошибка ввода\n')
                continue
            day_number = 1
            cur_distance = a
            print('1-й день:', cur_distance)
            while cur_distance < b:
                cur_distance *= 1.1
                day_number += 1
                print('{}-й день: {}'.format(day_number, round(cur_distance, 2)))

            print()
            print('Ответ: на {}-й день спортсмен достиг результата не менее {} км.\n'.format(day_number, b))
            a = ''
            b = ''

