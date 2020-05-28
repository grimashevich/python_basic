"""
Модуль с моими функциями
Версия 0.1
Дата 26.05.20
"""


def isfloat(value, must_be_pos=None):
    """Проверяет является ли значение float
    
    value -- Значение, которое нужно проверить
    must_be_pos --  True если проверяемое значение должно быть положительным
                    False если проверяемое значение должно быть отрицательным
                    None если принадлежность числа не проверяется
    """
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