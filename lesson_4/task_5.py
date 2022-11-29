"""
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
Например:


"""


import sys

from task_4 import rate


def show_rate(*args):
    if args:
        print(rate(args[0]))
        return 0
    return 1


if __name__ == '__main__':
    exit(show_rate(*sys.argv[1:]))
