"""
 *(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи те же, а значения — кортежи вида (<files_quantity>,
[<files_extensions_list>]), например:

{
100: (15, ['txt']),
1000: (3, ['py', 'txt']),
10000: (7, ['html', 'css']),
100000: (2, ['png', 'jpg'])
}

Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили
скрипт

"""


import os
import operator


def get_key(num):
    result = 10
    while num >= 10:
        num = num // 10
        result *= 10
    return result


def show_stat(given_path):
    stat = {}
    for root, dirs, files in os.walk(given_path):
        for file in files:
            file_path = os.stat(os.path.join(root, file))
            key = get_key(file_path.st_size)
            if key in stat.keys():
                stat[key] += 1
            else:
                stat[key] = 1
            ext = file.rsplit('.', maxsplit=1)[-1].lower()

    stat = dict(sorted(stat.items(), key=operator.itemgetter(0)))
    for key, value in stat.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    chop_project = r'C:\projects\chop_project\chop'
    show_stat(chop_project)
