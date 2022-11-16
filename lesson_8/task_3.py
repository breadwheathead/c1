"""
Написать декоратор для логирования типов позиционных аргументов функции, например:

def type_logger...
...
@type_logger
def calc_cube(x):
return x ** 3
 a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете
ли вы вывести тип значения функции? Сможете ли решить задачу для именованных
аргументов? Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя
функции, например, в виде:

 a = calc_cube(5)
calc_cube(5: <class 'int'>)

"""
from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args, **kwargs):
        print(type(callback()))
        args_log = {arg: type(arg) for arg in args}
        kwargs_log = {kwarg: type(kwarg) for kwarg in kwargs.values()}
        args_log.update(kwargs_log)
        print(wrapper.__name__, args_log)
        return callback(*args, **kwargs)

    return wrapper


@type_logger
def calc_cube(*args, **kwargs):
    result_args = [arg ** 3 for arg in args]
    result_kwargs = [kwarg ** 3 for kwarg in kwargs.values()]
    result_args.extend(result_kwargs)
    return result_args


if __name__ == '__main__':
    print(calc_cube(2, 3, 4, n=5, m=6))
