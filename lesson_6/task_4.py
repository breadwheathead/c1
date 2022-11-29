"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
двоеточие и пробел после ФИО:

Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи

"""
from sys import getsizeof
from itertools import zip_longest

USERS = ('Пшеничников,Алексей,Валерьевич', 'Пшеничников,Никита,Валерьевич', 'Пшеничников,Виктор,Валерьевич', 'Пшеничников,Илья,Валерьевич')
HOBBIES = ('горные лыжи', 'скалолазание,охота', 'рыбалка,фотография,рисование')


def create_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))


def merge_to_one(users_file, hobbies_file, destination_file):
    with open(users_file, 'r', encoding='utf-8') as file:
        users = [row.strip().replace(',', ' ') for row in file]

    with open(hobbies_file, 'r', encoding='utf-8') as file:
        hobbies = [row.strip().replace(',', ', ') for row in file]

    if len(users) < len(hobbies):
        return 1

    with open(destination_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join((f'{user}: {hobby}' for user, hobby in zip_longest(users, hobbies))))


if __name__ == '__main__':
    # create_file('users.csv', USERS)
    # create_file('hobbies.csv', HOBBIES)
    users = 'users.csv'
    hobbies = 'hobbies.csv'
    destination = 'users_hobbies.txt'
    exit(merge_to_one(users, hobbies, destination))
