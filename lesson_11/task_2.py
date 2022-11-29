"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой

"""


class CustomZeroDivisionError(ZeroDivisionError):
    pass


if __name__ == '__main__':
    try:
        a = 1
        b = int(input('введите не 0: '))
        if b == 0:
            raise CustomZeroDivisionError('ай')
    except CustomZeroDivisionError as e:
        print(e, 'На ноль можно делить, но нельзя иногда!')
