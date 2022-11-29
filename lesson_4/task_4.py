"""
4. Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
функции currency_rates(). Убедиться, что ничего лишнего не происходит

"""

import requests
import re
from decimal import Decimal
from datetime import date


def rate(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    # print(content)

    cur_date = re.search(r'(?P<day>\d{2}).(?P<month>\d{2}).(?P<year>\d{4})', content)
    cur_date = {k: int(v) for k, v in cur_date.groupdict().items()}
    cur_date = date(year=cur_date['year'], month=cur_date['month'], day=cur_date['day'])

    template = re.compile(
        fr'{currency.upper()}</CharCode><Nominal>(?P<nominal>\d+)</Nominal><Name>\w+\s?\w+?</Name><Value>(?P<value>\d+,\d*)</Value>')
    result_rate = re.search(template, content)
    if not result_rate:
        return None
    result_rate = {k: Decimal(v.replace(',', '.')) for k, v in result_rate.groupdict().items()}
    result_rate = result_rate['value'] / result_rate['nominal']

    return cur_date, result_rate


if __name__ == '__main__':
    usd_rate = rate('usd')
    evr_rate = rate('eur')
    uzs_rate = rate('uzs')
    fictional_rate = rate('fictional')
    for rate in (usd_rate, evr_rate, uzs_rate, fictional_rate):
        print(rate)
