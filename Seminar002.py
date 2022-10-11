# Задача 0. Дано число N. найти все енр делители.
# Для каждого делителя укажите чётный он или не чётный.


# def CheckEven(x):
#     if x % 2 == 0:
#             return("- чётный")
#     else:
#             return("- нечётный")  

# def Zadacha0():         
#  number = 60
#  for i in range(1, number + 1):
#        if number % i == 0:
#            print(i, end=" ")
#            print(CheckEven(i))  
# Zadacha0()


# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.

# print("x | y | ¬ X ∨ Y")
# for x in range(0,2):
#     for y in range(0,2):
#         sum = not x or y
#         print(f"{x} | {y} | {int(sum)}")
        

# Задача 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другую.

string_1 = input()
string_2 = input()
if len(string_1) > len(string_2):
    print(string_1)
    count = 0
    for i in range(len(string_1)):
            print(string_1[ i : i + len(string_2)])
            if string_2 ==string_1[i:i+len(string_2)]:
                count +=1
print("количество совпадений строк", count) 
    
