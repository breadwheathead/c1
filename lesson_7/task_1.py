"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
|--settings
|--mainapp
|--adminapp
|--authapp


"""

import os


def starter():
    root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    dirs = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
    for dr in dirs:
        if not os.path.exists(os.path.join(root, dr)):
            os.mkdir(os.path.join(root, dr))


if __name__ == '__main__':
    starter()
