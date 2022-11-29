"""
3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса
дату, которая передаётся в ответе сервера. Дата должна быть в виде объекта date. Подумайте,
как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?


"""
from datetime import datetime
import requests


def currency_rates(code=None):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    content_list = content.split('ID')
    currency_date = content_list[0].split('Date=')[-1][1:11].split('.')
    currency_date.reverse()
    currency_date = '-'.join(currency_date)
    currency_date = datetime.strptime(currency_date, '%Y-%m-%d')

    for row in content_list:
        if code.upper() in row:
            value = float(row.split('Value')[1][1:-2].replace(',', '.'))
            nominal = float(row.split('Nominal')[1][1:-2])
            result = round(value / nominal, 6)
            return currency_date, result


print(currency_rates('uzs'))
