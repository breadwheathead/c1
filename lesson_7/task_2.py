"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей
структурой:

|--my_project
|--settings
| |--__init__.py
| |--dev.py
| |--prod.py
|--mainapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
| |--mainapp
| |--base.html
| |--index.html
|--authapp
| |--__init__.py
| |--models.py
| |--views.py
| |--templates
| |--authapp
| |--base.html
| |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом
текстовом редакторе «руками» (не программно); предусмотреть возможные исключительные
ситуации, библиотеки использовать нельзя.

my_project/settings/__init__.py


"""

import os
import yaml

from custom_errors import EmptyFileError

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
STARTER_FILE_NAME = 'config.yaml'
VALID_EXTENSIONS = ('.py', '.html', '.css')

TEMPLATE = [
    {'my_project': [
        {'settings': [
            '__init__.py',
            'dev.py',
            'prod.py'
        ]},
        {'mainapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {'templates': [
                {'mainapp': [
                    'base.html',
                    'index.html']}]}]},
        {'authapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {'templates': [
                {'authapp': [
                    'base.html',
                    'index.html']}]}]}]}
]

PATHS = [
    'my_project/settings/__init__.py',
    'my_project/settings/def.py',
    'my_project/settings/prod.py',
    'my_project/mainapp/__init__.py',
    'my_project/mainapp/models.py',
    'my_project/mainapp/views.py',
    'my_project/mainapp/templates/mainapp/base.html',
    'my_project/mainapp/templates/mainapp/index.html',
    'my_project/authapp/__init__.py',
    'my_project/authapp/models.py',
    'my_project/authapp/views.py',
    'my_project/authapp/templates/authapp/base.html',
    'my_project/authapp/templates/authapp/index.html'
]


def create_starter_file(file_name: str, template: list):
    with open(file_name, 'w', encoding='utf-8') as file:
        yaml.dump(template, file)
    print('OK')


def deploy_starter(file_name):
    """создает стартер проекта в виде файлов и папок"""
    try:
        if os.stat(file_name).st_size == 0:
            raise EmptyFileError
        with open(file_name, 'r', encoding='utf-8') as file:
            template = yaml.load(file, Loader=yaml.FullLoader)
            monster_create(get_paths(template))
    except FileNotFoundError:
        print(f'Файл с именем {file_name} не найден!')
    except EmptyFileError:
        print('Файл пуст!')


def monster_create(list_path):
    """создаёт структуру по списку путей"""
    for path in list_path:
        dir_path = os.path.join(ROOT, path.rsplit('/', maxsplit=1)[0])
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        if path.endswith(VALID_EXTENSIONS):
            create_file(path)


def get_paths(template: list):
    """панимуляция с созданием списка путей из структуры исходного списка"""
    paths = []
    for item in template:
        if isinstance(item, str):
            paths.append(f'{item}')
        elif isinstance(item, dict):
            parent = next(key for key in item.keys())
            if item.get(parent):
                for child in get_paths(item.get(parent)):
                    paths.append(f'{parent}/{child}')
            else:
                paths.append(f'/{parent}/')
        else:
            raise TypeError(f'Неверный тип данных: {item}: {type(item)}')

    return paths


def create_file(file_path: str):
    file = open(file_path, 'w')
    file.close()


if __name__ == '__main__':
    # create_starter_file(STARTER_FILE_NAME, TEMPLATE)
    deploy_starter(STARTER_FILE_NAME)
