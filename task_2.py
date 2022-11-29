"""
*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
ключевое слово yield.

"""

nums = 15
result = (num for num in range(1, nums + 1, 2))
print(next(result))
print(next(result))
print(*result)