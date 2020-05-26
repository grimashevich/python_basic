"""
3.Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


def sum_of_max2(a: float, b: float, c: float):
    return a + b + c - min(a, b, c)


print(sum_of_max2(2, 5, -1))
