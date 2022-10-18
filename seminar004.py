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