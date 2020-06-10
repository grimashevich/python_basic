"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых
математических величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий
шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку
метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения
должна быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д. """


class Matrix:
    def __init__(self, data: list):
        self.__data = data

    def __str__(self):
        result = '\n'
        max_w = len(str(max(map(max, self.__data))))
        print(max(self.__data))
        for itm in self.__data:
            for itm2 in itm:
                result += str(itm2).center(max_w + 4, ' ') + ' '
            result += '\n\n'
        return result

    def __add__(self, other):
        a = self.__data
        b = other.__data

        # Дополняет матрицы разных размеров нулями. Понимаю, что костыли, но пока - как смог.
        c_width = max(len(a[0]), len(b[0]))
        c_height = max(len(a), len(b))

        if len(a[0]) < c_width:
            tmp = [0 for _ in range(len(a[0]), c_width)]
            for l_a in a:
                l_a.extend(tmp)

        if len(b[0]) < c_width:
            tmp = [0 for _ in range(len(b[0]), c_width)]
            for l_a in b:
                l_a.extend(tmp)

        for _tmp in range(len(a), c_height):
            a.append([0 for _ in range(c_width)])

        for _tmp in range(len(b), c_height):
            b.append([0 for _ in range(c_width)])
        # Конец дополнения нулями

        i = 0
        for itm_a in a:
            j = 0
            for itm_a2 in itm_a:
                b[i][j] += itm_a2
                j += 1
            i += 1
        return Matrix(b)


l1 = [[1, 2, 3, 4, 5, 6],
      [1, 2, 3, 4, 5, 6],
      [1, 2, 3, 4, 5, 6],
      ]

l2 = [[3, 2, 1],
      [1, 2, 3],
      [1, 2, 3],
      [4, 4, 4],
      [5, 5, 5],
      [6, 6, 6],
      ]

x = Matrix(l1)
y = Matrix(l2)
z = x + y
print(z)
