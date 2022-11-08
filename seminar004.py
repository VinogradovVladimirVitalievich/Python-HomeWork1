# import random
# numbers =[] * 10
# phrase = "abcd"
# for i in range(10):
#     numbers.append(random.randint(1, 10)) 
# print(numbers)

# # добавление файла
# # or

# data = open("numbers.txt", "w")
# data.writelines(str(numbers))
# data.close()

# #or 

# with open("numbers.txt", "w") as data:
#     data.writelines(str(numbers))
#     data.writelines(phrase + "/n")
# print(numbers)

# Задача 1. Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу. 
# переменная tuple - обозначение кортежа

# import random
# def chenge_index(numbers, index):
#     numbers = list(numbers)
#     numbers[index - 1] = random.randint(10, 100)
#     numbers = tuple(numbers)
#     return(numbers)
# size = random.randint(5, 12)
# numbers = tuple(random.randint(10, 100) for i in range(10))
# print(numbers)
# index = int(input("Введите индекс, который необходимо заменить: "))
# print(chenge_index(numbers, index))


# Задача 2. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». На главную роль нужен актёр обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль. Списки актёров поместите в соответствующие файлы.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад
# def openFile(nameFile):
#     f = open(nameFile, encoding='utf-8')
#     phrase = f.readlines()
#     f.close()
#     list = phrase[0].split()
#     return set(list)

# beauty = openFile('beauty.txt')
# strong = openFile('strong.txt')
# smart = openFile('smart.txt')

# print(beauty.intersection(smart).intersection(strong))

# Задача 3. Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов. Удалите из списка дубликаты уже имеющихся элементов.

# import random

# def GetNumbers():
#     data = open("list.txt", "w")
#     numbers = [random.randint(1 ,20) for i in range(0, 10)]
#     data.write(str(numbers))
#     print(numbers)
#     data.close
# GetNumbers()

# def FindeDublicate():
#     data = open("list.txt", "r", encoding="utf-8")
#     num = data.readline()[1:-1].split(", ")
#     num = [int(i) for i in num]
#     num = set(num)
#     print(type(num),num)
# FindeDublicate() 

##4 задача
# import math
# radius = 15
# print(round(math.pi * math.pow(radius, 2), 2))

# from cmath import pi
# print(pi)