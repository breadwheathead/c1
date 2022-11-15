"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
«руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
templates, например:

|--my_project
...
|--templates
| |--mainapp
| | |--base.html
| | |--index.html
| |--authapp
| |--base.html
| |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы
расположены в родительских папках (они играют роль пространств имён); предусмотреть
возможные исключительные ситуации; это реальная задача, которая решена, например, во
фреймворке django.

"""

import os
import shutil

from custom_errors import DirectoryNotFound

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
DIR = 'my_project'


def move_templates_root(dir_path):
    """собирает все шаблоны в одну директорию templates"""
    new_dir_name = 'templates'
    new_dir = os.path.join(dir_path, new_dir_name)

    try:
        for root, _, _, in os.walk(dir_path):
            if root.endswith('templates'):
                shutil.move(root, new_dir)
    except shutil.Error as e:
        print('Корневая директория templates уже создана!')
    except Exception as e:
        print(e.args)


if __name__ == '__main__':
    destination_path = os.path.join(ROOT, DIR)
    if os.path.exists(destination_path):
        move_templates_root(destination_path)
    else:
        raise DirectoryNotFound(f'Директория {DIR} не найдена!')
