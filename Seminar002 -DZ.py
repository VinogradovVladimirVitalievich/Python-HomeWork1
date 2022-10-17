# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('input N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')



# Задача 2. Выведите таблицу истинности для выражения ¬(not)(X ∧(and) Y) ∨(or) Z. 

# print("x | y | z ¬(X ∧ Y) ∨ Z")
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range (0,2):
#          sum = not (x and y) or z
#         print(f"{x} | {y} | {z} | {int(sum)}")



# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def LikeSymbols(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    list = []
    str3 = None
    for i in range(len1):
        count = 0
        for j in range(len2):
            if str1[i] == str2[j]:
                count += 1
        str3 = f"{str1[i]} - {count}"
        list.append(str3)
    return list
str1 = 'one'
str2 = 'onetwonine'
print(LikeSymbols(str1, str2))


    



# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]