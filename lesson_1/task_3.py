"""
3. Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов», задаем
число 2 — получаем «2 процента». Вывести все склонения для проверки.

"""


def percent(n):
    if 0 < n <= 20:
        result = f'{n} процент'
        if n in range(2, 5):
            result += 'а'
        if n in range(5, 21):
            result += 'ов'
        return result
    raise ValueError


if __name__ == '__main__':
    try:
        num = int(input('введите число: '))
        print(percent(num))

    except ValueError as e:
        print('Принимаются только натуральные числа от 1 до 20!')
