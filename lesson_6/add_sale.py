import sys
import re


def validator(revenue: list):
    for item in revenue:
        if not re.match(r'\d+[.,]?\d*$', item):
            raise TypeError(f'{item} - не число! Отказ записи во избежание путаницы')
    return revenue


def add_sale(args):
    program, *revenue = args
    if not revenue:
        raise Exception('Вы ничего не ввели!')
    revenue = validator(revenue)
    with open('bakery.csv', 'a', encoding='utf-8') as file:
        file.writelines(list(map(lambda value: f"{value.replace(',', '.'):<10}\n", revenue)))
    return 0


if __name__ == '__main__':
    exit(add_sale(sys.argv))
