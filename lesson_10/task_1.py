"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр

"""


class SumMatrixError(Exception):
    def __str__(self):
        return '{}: Матрицы не соразмерны! Сложение невозможно!'.format(__class__.__name__)


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda row: '  '.join(map(str, row)), self.matrix))

    def __len__(self):
        return sum([len(row) for row in self.matrix])

    def __add__(self, other):
        if len(self) != len(other):

            raise SumMatrixError

        result = []
        for row_x, row_y in zip(self.matrix, other.matrix):
            row = []
            for x, y in zip(row_x, row_y):
                row.append(x + y)
            result.append(row)

        return self.__class__(result)

    def __radd__(self, other):
        if not isinstance(other, __class__):
            return self
        return self.__add__(other)


if __name__ == '__main__':
    m1 = Matrix([[1, 3, 2], [2, 0, 9], [5, 5, 1]])
    m2 = Matrix([[5, 6, 0], [2, 5, 4], [6, 8, 0]])
    m3 = Matrix([[5, 8, 1], [4, 2, 3], [1, 1, 0]])

    print(m1)
    # print(len(m1))
    print()
    print(m2)
    # print(len(m2))
    print()
    print(m3)
    # print(len(m3))
    print('----')

    try:
        print(m2 + m3 + m1)
        print()
        print(sum([m2, m1, m3]))
    except SumMatrixError as e:
        print(e)
