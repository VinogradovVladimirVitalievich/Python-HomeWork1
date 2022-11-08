# Урок 4. Данные, функции и модули в Python. Продолжение


# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

# import math


# def get_int_number(): return int(input())


# def check_prime(n: int, divigers: list):
#     if n % 2 == 0:
#         divigers.append(2)
#         return n // 2
#     if n % 3 == 0:
#         divigers.append(3)
#         return n // 3
#     for i in range(1, math.ceil(n ** 0.5) + 1):
#         if n % (6 * i - 1) == 0:
#             divigers.append(6 * i - 1)
#             return n // (6 * 1 - 1)
#         if n % (6 * i + 1) == 0:
#             divigers.append(6 * i + 1)
#             return n // (6 * i + 1)


# def find_divigers(number: int):
#     divigers = []
#     while number != 1:
#         number = check_prime(number, divigers)
#     return divigers


# def main():
#     n = get_int_number()
#     divigers = find_divigers(n)
#     print(f'prime divigers of {n}:\n',*divigers)


# if __name__ == '__main__':
#     main()


# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.3 -> 3.142
# 5 -> 3.14159

# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x2. 3x^2 + x + 8Результат: 8x^2 + 4x + 8