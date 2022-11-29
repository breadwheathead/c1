import os
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))


def delete_directory():
    dir_name = 'my_project'
    dir_path = os.path.join(ROOT, dir_name)
    shutil.rmtree(dir_path)
    print('OK')


if __name__ == '__main__':
    delete_directory()
