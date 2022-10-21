# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8


# firstnumber = 0
# secondnumber = 1
# count = 1000
# data = open("fibonachi.txt", "w")
# for i in range(count):
#     data.writelines(str(firstnumber)+ "\n")
#     (firstnumber, secondnumber) = (secondnumber, firstnumber + secondnumber)



# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

# with open("Fruits.txt", encoding = "utf-8") as data:
#     Fruits = data.readline().split()    
#     print(Fruits)
#     letter = "а"
#     for i in Fruits:
#         if i[0].lower() == letter.lower():
#             print(i)

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

from multiprocessing.resource_sharer import stop


dictionary = \
    {
        "Привет" : "Салют!", "Как тебя зовут?" : "Меня зовут Владимир", "Выход": "Пока!"
    }
isStarted = True
while isStarted:
    answer = input("Я: ")
    if answer == " выход":
        isStarted = not isStarted
    if answer in dictionary.keys():
        print("Бот:", dictionary[answer])
    else:
        print("Бот: неизвестная команда, попробуйте снова")
        break
stop