"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
предыдущего, например:

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 155]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
сделать оптимизацию кода по памяти, по скорости

"""
from sys import getsizeof
from time import perf_counter
from itertools import islice

src = [3000, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

for i in range(1, len(src)):
    if src[i - 1] < src[i]:
        print(src[i], end=' ')

print()
start = perf_counter()
for num, next_num in zip(src, src[1:]):
    if num < next_num:
        print(next_num, end=' ')

print()
print(*islice((next_num for num, next_num in zip(src, src[1:]) if num < next_num), 20))

print(getsizeof(src))
print(perf_counter() - start)


