"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
логов из предыдущего задания

Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
даже с файлами, размер которых превышает объем ОЗУ компьютера.

"""
from itertools import islice

import requests
import re
import operator
from time import perf_counter

PATH = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'


def get_content():
    """
    Запрашивает данные с указанного интернет-адреса и возвращает ответ в виде строки
    :return: response: str
    """
    response = requests.get(PATH)
    return response.content.decode(encoding=response.encoding)


def read_file():
    """
    Читает файл и возвращает содержимое в виде строки
    :return: content: str

    """
    content = ''
    with open('nginx_logs.txt', 'r', encoding='utf-8') as file:
        for row in file:
            content += row
    return content


def get_addresses(logs):
    template = re.compile(r'\d+\.\d+\.\d+\.\d+')
    return re.findall(template, logs)


def get_spammer(addresses):
    addresses_counts = {}
    for address in addresses:
        if address not in addresses_counts.keys():
            addresses_counts[address] = 1
        addresses_counts[address] += 1
    max_value = max(addresses_counts.values())
    spammer = next((k, v) for k, v in addresses_counts.items() if v == max_value)
    return spammer


if __name__ == '__main__':
    start = perf_counter()
    content = get_content()
    print('spammer:', get_spammer(get_addresses(content)))
    print(perf_counter() - start)
