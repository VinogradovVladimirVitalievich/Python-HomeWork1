# Start seducation
# ctrl+/  - закоментировать 

#1-Напишите программу которая на вход принимает число и выдаёт его квадрат

# number = input("Enter number: ")
# number = int(number)
# print(number * number)
# print(f"{number} * {number} = {number**2}")


# 2-Дано 2 числа, необходимо проверить является 1 число квадратом другого

# a = 25 
# b = 5
# if a**2 == b or b**2 == a:
#     print("YES")
# else:
#     print("NO")    


# организуйте последовательность ввод чисел до тех пор пока не будет 0
# Подсчитайте среди введённых чисел те который кратны 3

# number = None 
# count = 0
# while number != 0:
#     number = int(input("enter number: "))
#     if number % 3 ==0 and number != 0:
#       count +=1 
# print("enter end") 
# print("quantity numbers:  ", count)


# Напишите программу, которая будет на вход принимать число N и выводит числа от -N до N

# numbers = int(input("Enter number: "))
# N = range(-numbers, numbers+1)
# print(*N)

# or

# import math
# numbers = float(input("enter number: "))
# x = math.floor(numbers)
# x = abs(math.floor(numbers))
# for i in range (-x, x+1):
#   print(i, end= " ")


# Напишите программу, которая будет принимать на вход дробь и показывает первую цифру дробной части числа

# def find_digit():
#     n = float(input())
#     f1_part = int(n) - n
#     print(n)

# Напишите программу, которая находит наибольшее и наименьшее число из списка значений

# numbers = [int(e1) for e1 in input().split()]
# print(f'max = {max(numbers)}')
# print(f'min = {min(numbers)}')
