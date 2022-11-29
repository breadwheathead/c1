"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном
списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([item for item in src if src.count(item) == 1])  # O(n^2)

uniq_nums = set()
tmp_nums = set()

for item in src:
    if item not in tmp_nums:
        uniq_nums.add(item)
    else:
        uniq_nums.discard(item)
    tmp_nums.add(item)

print([num for num in src if num in uniq_nums])
