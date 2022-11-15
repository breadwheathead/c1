"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:

{
100: 15,
1000: 3,
10000: 7,
100000: 2
}

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


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

    stat = dict(sorted(stat.items(), key=operator.itemgetter(0)))
    for key, value in stat.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    chop_project = r'C:\projects\chop_project'
    show_stat(chop_project)
