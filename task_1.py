"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...


"""

import sys
from time import perf_counter
from itertools import islice


def odd_gen(nums):
    for num in range(1, nums + 1, 2):
        yield num


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci(nums):
    if nums in (1, 2):
        return 1
    elif nums == 0:
        return 0
    return fibonacci(nums - 1) + fibonacci(nums - 2)


odd_result = odd_gen(15)
print(next(odd_result))
print(*odd_result)

print(fibonacci(10))

result = fib_gen()
print(next(result))
print(next(result))
print(next(result))
print(*islice(result, 30))
