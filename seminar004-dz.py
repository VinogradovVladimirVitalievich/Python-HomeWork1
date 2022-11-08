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

# with open('icecream.txt', 'r', encoding='utf-8') as inf:
#     assortment = set(inf.readline().rstrip().split(', '))
#     current = set(inf.readline().rstrip().split(', '))
#     print(f'Закончилось:', *assortment - current)

# Задача 3. Выведите число π с заданной точностью. Точность вводится пользователем в виде натурального числа.3 -> 3.142
# 5 -> 3.14159

# from math import pi as PI
# from random import uniform as ru


# def get_int_number(*args): return int(input(*args))


# def print_pi(pi, dg):
#     print(round(pi, dg))


# def finding_pi():
#     n = 10 ** 7  # количество испытаний
#     k = 0  # количество точек внутри фигуры
#     s0 = 4  # площадь квадрата в котором фигура
#     print('waiting for counting PI')
#     for _ in range(n):
#         x = ru(-1, 1)
#         y = ru(-1, 1)

#         if x ** 2 + y ** 2 <= 1:
#             k += 1
#     print('DONE')
#     return (k / n) * s0


# def main():
#     n = get_int_number('how many digits in PI: ')
#     var = get_int_number('1 to math.PI, else to Monte Carlo finding PI: ')
#     if var == 1:
#         print_pi(PI, n)
#     else:
#         print_pi(finding_pi(), n)


# if __name__ == '__main__':
#     main()