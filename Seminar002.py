# Задача 0. Дано число N. найти все енр делители.
# Для каждого делителя укажите чётный он или не чётный.

def zadacha0():
    number = 60
    for i in range(1, number + 1):
       if number % i == 0:
           print(i, end = " ")
           if i % 2 == 0:
            print(" - чётный")
           else:
            print(" - нечётный")   
