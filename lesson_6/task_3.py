"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи

"""

USERS = ['Иванов,Иван,Иванович\n', 'Петров,Петр,Петрович\n', 'Пшеничников,Илья,Валерьевич\n',
         'Пшеничников,Алексей,Валерьевич\n', 'Пшеничников Никита Валерьевич\n', 'Пшеничников Виктор Валерьевич']
HOBBIES = ['горные лыжи\n', 'скалолазание,охота\n', 'рыбалка,фотография,рисование\n', 'походы']


def create_file(filename: str, data: list):
    with open(f'{filename}.csv', 'w', encoding='utf-8') as file:
        file.writelines(data)


def create_pairs():
    with open('users_hobbies.csv', 'w', encoding='utf-8') as file:
        users = open('users.csv', 'r', encoding='utf-8')
        hobbies = open('hobbies.csv', 'r', encoding='utf-8')

        _users = (user for user in map(lambda row: row.strip().replace(',', ' '), users.readlines()))
        _hobbies = (hobby for hobby in map(lambda row: row.strip().replace(',', ', '), hobbies.readlines()))

        result = {user: hobby for hobby, user in zip(_hobbies, _users)}
        result.update({user: None for user in _users})
        rows = '\n'.join((f'{k}: {v}' for k, v in result.items()))
        file.write(rows)

        users.close()
        hobbies.close()


if __name__ == '__main__':
    create_file('users', USERS)
    create_file('hobbies', HOBBIES)
    create_pairs()
