"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
web-сервера nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)

— получить список кортежей вида: (<remote_addr>, <request_type>,

<requested_resource>). Например:

[
...
('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...
]

"""
from time import perf_counter

import requests
import re

PATH = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'


def get_content():
    response = requests.get(PATH)
    content = response.content.decode(encoding=response.encoding)
    return content


def write_file(path):
    with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
        f.write(get_content(path))


def read_file():
    content = ''
    with open('nginx_logs.txt', encoding='utf-8') as f:
        # content = f.read(1343)
        content = f.read()
        # while True:
        #     chunk = f.read(100)
        #     content += chunk
        #     if not chunk:
        #         break
    return content


def parser(content):
    template = re.compile(r'(\d+\.\d+\.\d+\.\d+|\w+:\w+:\w+:\w+:\w+:\w+:\w+:\w+)'
                          r' - - \[\d+/\w+/\d{4}:\d{2}:\d{2}:\d{2} \+0{4}\] "'
                          r'(GET|HEAD)'
                          r' '
                          r'(/downloads/product_[12])')

    result = (re.findall(template, content))
    return result


if __name__ == '__main__':
    start = perf_counter()

    for i, log in enumerate(parser(get_content())):
        print(i, log)

    print('------------')
    print(perf_counter() - start)
