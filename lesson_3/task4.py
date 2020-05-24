"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
необходимо обойтись без встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя
способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
"""


def isfloat(value, must_be_pos=None):
    """Проверяет является ли значение float"""
    try:
        float(value)
        if must_be_pos and float(value) <= 0 or must_be_pos is False and float(value) >= 0:
            # Не уверен можно ли строить троичные конструкции на основании True, False и None, но вроде работает
            #                                           Явно задан must_be_pos is False, т.к. not None дает True
            return False
        return True
    except ValueError:
        return False


def isinteger(value, must_be_pos=None):
    """Проверяет является ли значение value целым числом

    value -- Значение, которое нужно проверить
    must_be_pos --  True если проверяемое значение должно быть положительным
                    False если проверяемое значение должно быть отрицательным
                    None если принадлежность числа не проверяется
    """
    try:
        int(value)
        if must_be_pos and int(value) <= 0 or must_be_pos is False and int(value) >= 0:
            # Не уверен можно ли строить троичные конструкции на основании True, False и None, но вроде работает
            #                                           Явно задан must_be_pos is False, т.к. not None дает True
            return False
        if int(value) % 1 != 0:
            return False
        return True
    except ValueError:
        return False


# Вариант с циклом
def my_func(x, y):
    value = x
    for tmp in range(0, y + 1, -1):
        value *= x
    return 1 / value


# Вариант с оператором **
def my_func2(x, y):
    return x ** y


while True:
    try:
        my_x, my_y = input('Введите действительное x>0 и целое y<0 через пробел ').split(' ')
        if isfloat(my_x, True) and isinteger(my_y, False):
            break
    except ValueError:
        continue

my_x, my_y = float(my_x), int(my_y)
print('Результат решения через цикл: ', my_func(my_x, my_y))
print('Результат решения через **:   ', my_func2(my_x, my_y))
