"""
2. Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем
включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические
операции! К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых
делится нацело на 7. Внимание: новый список не создавать!!!

"""

# sum_result = 17485588610
# sum_result = 15392909930


def divider(n):
    sum = 0
    while n:
        sum += n % 10
        n = n // 10
    return sum


def summary(array):
    result = 0
    for num in array:
        if not divider(num) % 7:
            result += num
    return result


numbers = [num ** 3 for num in range(1, 1000, 2)]
print(numbers[:10])

print('-----')
print(summary(numbers))

numbers = [num + 17 for num in numbers]
print(numbers[:10])

print('----')
print(summary(numbers))
