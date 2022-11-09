"""
7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
которой не существует.


"""

import sys

from add_sale import validator


def update_sale(args):
    revenue = validator([args[1]])[0]
    with open('bakery.csv', 'r+', encoding='utf-8') as file:
        file.seek((int(args[0]) * 12) - 12)
        file.write(f"{revenue.replace(',', '.'):<10}")
    return 0


if __name__ == '__main__':
    exit(update_sale(sys.argv[1:]))
