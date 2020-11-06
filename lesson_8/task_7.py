"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. """

from copy import copy


def is_float(a: str) -> bool:
    try:
        float(a)
    except ValueError:
        return False
    else:
        return True


class ComplexNumberError(ValueError):
    def __init__(self, txt):
        self.text = txt


class ComplexNumber:
    def __init__(self, numb: str):
        c_number = []
        numb = numb.replace(' ', '')

        if numb.find('i') != -1:
            numb = numb.replace('-', '+-')
            c_number = numb.split('+', maxsplit=1)
        else:
            c_number.append(numb)
            c_number.append('0')

        if c_number[0] == '':
            _ = c_number.pop(0)

        if len(c_number) == 0:
            raise ComplexNumberError('Комплексное число введено неверно')
        elif len(c_number) == 1:
            c_number.append('0')
            c_number[0], c_number[1] = c_number[1], c_number[0]

        if not is_float(c_number[0]):
            raise ComplexNumberError('Ошибка действительной части комплексного числа')
        else:
            self.__real = int(c_number[0]) if c_number[0].find('.') == -1 else float(c_number[0])

        if c_number[1] == '-i':
            c_number[1] = '-1i'
        c_number[1] = c_number[1].replace('i', '') if c_number[1] != 'i' else '1'
        if not is_float(c_number[1]):
            raise ComplexNumberError('Ошибка мнимой части комплексного числа')
        else:
            self.__im = int(c_number[1]) if c_number[1].find('.') == -1 else float(c_number[1])

    def __str__(self):
        if self.__im == 0:
            return str(self.__real)
        result = '' if self.__real == 0 else str(self.__real)
        result += '+' if self.__real != 0 and self.__im > 0 else ''
        if self.__im == -1:
            result += '-i'
        else:
            result += str(self.__im) + 'i' if self.__im != 1 else 'i'
        return result

    def __add__(self, other):
        res = copy(self)
        res.__real += other.__real
        res.__im += other.__im
        return res

    def __mul__(self, other):
        res = copy(self)
        res.__real = self.__real * other.__real + self.__im * other.__im * -1
        res.__im = self.__real * other.__im + self.__im * other.__real
        return res


z1 = ComplexNumber('-i')
z2 = ComplexNumber('7+8i')
print(f'Сумма: ({z1}) + ({z2}) =', z1 + z2)
print(f'Произведение: ({z1}) * ({z2}) =', z1 * z2)
