"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError. Пример:

email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
email_parse('someone@geekbrainsru')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
...
raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru

Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в
регулярном выражении; имеет ли смысл в данном случае использовать функцию
re.compile()?

"""

import re


def email_parse(email_address):
    pattern = re.compile(r'(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email_address)
    if result is None:
        raise ValueError(f'wrong email: {email_address}')
    return result.groupdict()


if __name__ == '__main__':
    try:
        print(email_parse('ilyapshenichnikon@yandex.ru'))
        print(email_parse('someone@geekbrainsru'))
    except ValueError as e:
        print(e)
        exit(1)
