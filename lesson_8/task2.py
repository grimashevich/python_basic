"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """


class MyZeroDivErr(ZeroDivisionError):
    def __init__(self, txt):
        self.text = txt


while True:
    try:
        a = input('Введите делимое: ')
        b = input('Введите делитель: ')
        a, b = int(a), int(b)
        if b == 0:
            raise MyZeroDivErr('Ошибка деления на 0')
        c = a / b
        print(c)
        break
    except MyZeroDivErr as e:
        print(e)
        continue
    except ValueError as e:
        print('ОШИБКА: ', e)
        continue

