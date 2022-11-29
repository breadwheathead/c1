"""
**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.

"""

import sys

from task_4 import merge_to_one


def cli(args):
    merge_to_one(*args)


if __name__ == '__main__':
    exit(cli(sys.argv[1:4]))
