"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.


"""
from decimal import Decimal

import requests

PATH = 'http://www.cbr.ru/scripts/XML_daily.asp'


def get_content():
    response = requests.get(PATH)
    content = response.content.decode(encoding=response.encoding)
    content_list = content.split('<CharCode>')
    return content_list


def currency_rates(code):
    rows = get_content()
    for row in rows:
        if row.startswith(code.upper()):
            result = Decimal(row.split('Value')[1][1:-2].replace(',', '.')) / Decimal(row.split('Nominal')[1][1:-2])
            return f'курс {code.upper()} {result} руб'
    return None


print(currency_rates('uzs'))

