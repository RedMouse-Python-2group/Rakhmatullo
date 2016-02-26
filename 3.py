# -*- coding: utf-8 -*-
# Laba 3.1.1
# x = int(raw_input("Введите число от 1 до 9:"))
#
#
# def povtorsroki():
#     print "1-3"
#     s = (raw_input("Введите строку:"))
#     n = int(raw_input("Введите число повторов строки:"))
#     print([s for i in range(n)])
#
#
# def stepen():
#     print "4-6"
#     m = int(raw_input("Введите степень"))
#     print(x ** m)
#
#
# def xplus10():
#     global x
#     print "7-9"
#     for i in range(10):
#         x += 1
#         print(x)
#
#
# if 1 <= x <= 3:
#     povtorsroki()
# elif 3 < x <= 6:
#     stepen()
# elif 6 < x <= 9:
#     xplus10()
# else:
#     print "Ошибка ввода"

# Laba 3.1.2
List = ['Общество в начале XXI века', 'Вам в детский сад', 'Вам в школу', 'Вам в профессиональное учебное заведение',
        'Вам на работу', 'Вам предоставляется выбор', 'Ошибка! Это программа для людей!']
print(List[0])
x = int(raw_input("возраст:"))
if 0 < x <= 7:
    print(List[1])
elif 7 < x <= 18:
    print(List[2])
elif 18 < x <= 25:
    print(List[3])
elif 25 < x <= 60:
    print(List[4])
elif 60 < x <= 120:
    print(List[5])
else:
    0 < x < 121
    for i in range(5):
        print(List[6])
