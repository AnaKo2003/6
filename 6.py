# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Было без лямбды:

n = int(input('Enter the number: '))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(factorial, end = ' ')

# Стало с лямбдой:

import math

a = int(input("Enter the number: "))
b = list(map(lambda x: math.factorial(x), range(1, a + 1)))
print(b)

# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# Было без лямбды:

n = int(input("Enter the n: "))
list = [round((1 + 1/n)**n, 2) for n in range(1, n + 1)]
print(list)
print(round(sum(list), 2))

# Стало с лямбдой (без округления):

n = int(input("Enter the n: "))
print(sum([((1 + 1/n)**n) for n in range(1, n)]))

