"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def isfloat(value):
    """Проверяет является ли значение float"""
    try:
        float(value)
        return True
    except ValueError:
        return False


def division(a: float, b: float) -> float:
    try:
        c = a / b
    except ZeroDivisionError:
        print('Ошибка, деление на 0')
        c = 0
    return c


x, y = '', ''
while not (isfloat(x) and isfloat(y)):
    x, y = input('Введите делимое и делитель, разделяя пробелом ').split(' ')
print(division(float(x), float(y)))
