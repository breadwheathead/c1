"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt

(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)

для получения информации вида: (<remote_addr>, <request_datetime>,
<request_type>, <requested_resource>, <response_code>, <response_size>),
например:

raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET
/downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET',
'/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки? Можно ли для них уточнить регулярное выражение?

"""

import requests
import re

PATH = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'


def get_content():
    response = requests.get(PATH)
    content = response.content.decode(encoding=response.encoding)
    return content


def parser(content):
    pattern = re.compile(r'(?P<remote_addr>(?:\d+\.){3}\d+|(?:\w+:){7}\w+)'
                         r'.*'
                         r'(?P<request_datetime>\d+/\w+/\d{4}(?::\d{2}){3})'
                         r'.*'
                         r'(?P<request_type>GET|HEAD)'
                         r'.*'
                         r'(?P<request_resourse>/downloads/product_[12])'
                         r'.*'
                         r'(?P<response_code>\d+)'
                         r'.*'
                         r'(?P<response_size>\d+)')

    result = pattern.finditer(content)
    if result is None:
        raise ValueError(f'Empty result!')
    return [m.groupdict() for m in result]


if __name__ == '__main__':
    for log in parser(get_content()):
        print(log)
