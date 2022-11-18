"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.

"""

import re
from datetime import datetime


class Date:
    def __init__(self, date_string: str):
        self.date_string = self.validator(date_string)

    def __str__(self):
        return self.date_string

    @staticmethod
    def mapper(date_string):
        pattern = re.compile(r'(\d{2})[./-](\d{2})[./-](\d{4})')
        result = pattern.fullmatch(date_string)
        if not result:
            raise TypeError('Строка не прошла преобразование!')
        return tuple(map(int, result.groups()))

    @staticmethod
    def validator(date_string):
        months = {
            31: {1, 3, 5, 7, 8, 10, 12},
            30: {4, 6, 9, 11},
            28: {2, }
        }
        day, month, year = Date.mapper(date_string)
        if not 1970 <= year <= datetime.now().year:
            raise TypeError('Неверный год! Год не меньше 1970!')
        for k, v in months.items():
            if month not in v:
                continue
            if 1 <= day <= k:
                return date_string
            raise TypeError('Неверное число!')
        else:
            raise TypeError('Неверный месяц!')


if __name__ == '__main__':
    date = Date('01/01/1970')
    print(date)
