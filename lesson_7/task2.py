"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property. """

from abc import ABC, abstractmethod


class ClothesAbstract(ABC):

    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size

    @abstractmethod
    def cloth_amount(self):
        pass


class Coat(ClothesAbstract):

    @property
    def cloth_amount(self):
        return self.size / 6.5 + 0.5

    @cloth_amount.setter
    def cloth_amount(self, cloth):
        _tmp = int((cloth - 0.5) * 6.5)
        self.size = _tmp if _tmp % 2 == 0 else _tmp - 1
        print(f'Для кол-ва ткани {cloth} установлен размер {self.size}')


class Suit(ClothesAbstract):

    @property
    def cloth_amount(self):
        return self.size * 2 + 0.3

    @cloth_amount.setter
    def cloth_amount(self, cloth):
        _tmp = int((cloth - 0.3) / 2)
        self.size = _tmp if _tmp % 2 == 0 else _tmp - 1
        print(f'Для кол-ва ткани {cloth} установлен размер {self.size}')


print('# Для пальто установлен размер 52')
coat = Coat('Пальто 1', 52)
print('Необходимое кол-во ткани:', coat.cloth_amount)
print('# Устанавливаем кол-во ткани = 8')
coat.cloth_amount = 8
print('\n')

print('# Для костюма установлен размер 54')
suit = Suit('Костюм', 54)
print('Необходимое кол-во ткани:', suit.cloth_amount)
print('# Устанавливаем кол-во ткани = 115')
suit.cloth_amount = 115
pass
