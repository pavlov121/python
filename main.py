# Занятие 2
# num1 = "2.5"
# num2 = 3
# res = float(num1) + num2
# print(res)
# from operator import truediv

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут", name, ". Мне ", age, " лет.", sep="") # sep - заменяет символы запятой на любые другие
# print("Меня зовут" + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне ", age, " лет.", sep="", end=" ")  # end - чем завершается print! (Перенос на другую строку)
# print("Меня зовут", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Новая строка")

# name = input("Ваше имя: ")
# print("Hello,", name)

# num = int(input("ведите число: "))
# power = int(input("ведите Степень: "))
# # res = int(num) ** int(power)
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)

# b1 = True # Пишутся в верхнем регистре
# b2 = False
# # print(b1, type(b1))
# print(b1 + 5)  # 1 + 5
# print(b2 + 5)  # 0 + 5

# print(bool("python")) # Когда что-то есть, то True
# print(bool("")) # Когда ничего нет, то False
# print(bool(None))

# False => "", 0, 0.0, False, None

# test = None
# print(test, type(test))
# test = 5
# print(test, type(test))

# print(7 == 7)
# print(2 + 5 == 7)
# print(2 + 5 == 7 + 3) #Сначала сложит то, что слева!
# print(7 != 10 - 3)
# print(8 > 5)
# print(8>=8)
#
# print("")
# print("hello" > "H{LLO")  # 104 > 72 (Кодировка символов!) Строки сравниваются посимвольно

# print(2 < 4 < 9) # True && True -> True
# print(2 * 5 > 7 >= 4 + 3) # 1) Арифметические операторы 2) Операторы сравнения
# print(3 * 3 <= 7 >= 2)

# print(5 - 3 == 2 and 1 + 3 == 4) # True: True => True
# print(5 - 3 == 2 and 1 + 3 < 4) # True: False => False
# print(5 - 3 > 2 and 1 + 3 ==4) # False: True => False

# print(5 - 3 == 2 or 1 + 3 == 4) # True: True => True
# print(5 - 3 == 2 or 1 + 3 < 4) # True: False => False
# print(5 - 3 > 2 or 1 + 3 ==4) # False: True => False

# print(not 9 - 7) #not 9 - 7 -> not 2 -> not True
# print(not 7 - 7)


# cnt = 5
# if cnt < 10:
#     cnt = cnt + 1 # Одна табуляция - 4-е пробела
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
#     print("Добро пожаловать")
#     # pass  # заглушка
# else:
#     print("Доступ запрещён")
#     ...  # - защита элемента!
#
# # pass, ... - заглушки


# import this
# print(this)

# a = 15
# b = 25
#
# if a > b:
#     print("a > b")
# elif b > a:  # Иначе -> если (else + if)
#     print("b > a")
# else:
#     print("a == b")

# a = int(input("Введите первую сторону: "))  # int - не обязательно! Сравниваем строки
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")

# Задача№1
# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5: # 1 <= day <= 5: (как диапазон) # (day >= 1) and day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресенье")
# else:
#     print("Такого дня недели не существует")

# Задача№2
# mes = int(input("Введите номер месяца: "))
# if 1 <= mes <= 12:
#     print("Есть такой месяц!")
#     if 1 <= mes <= 2 or mes == 12:
#         print("Зима")
#     if 3 <= mes <= 5:
#         print("Весна")
#     if 6 <= mes <= 8:
#         print("Лето")
#     if 9 <= mes <= 11:
#         print()
# else:
#     print("Нет такого месяца!")

# Задача№3

# n = int(input("ведите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# n = int(input("ведите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = 'user'
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:  # допустимый символ -> значение по умолчанию
#         print("пароль неверен")

# day = "вторник"
# time = 15
#
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# Задание 2
# Тернарные операторы

# a, b = 10, 20
# print(a if a < b else b)

# a, b = 10, 20
# print("a == b" if a == b else "a > b " if a > b else "a < b")

# Исключения
# a = 0
# b = "2"
# print(a + int(b))


# try:  # Попытаться
#     n = int(input("Введите: "))
#     print(12 / n)
# except ValueError:
#     print("Нельзя вводить  строки!")
# except ZeroDivisionError:
#     print("Нельзя делить на оль!")


# try:  # Попытаться
#     n = int(input("Введите: "))
#     print(12 / n)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или делить на ноль!")
# else:  # Отработает, если не возникло исключение!
#     print("Всё нормально. Вы ввели", n, sep=" ")
# finally:  # Отработает в любом случае!
#     print("Конец программы!")


# Задачка
# n = input("Введите первое число: ")
# m = input("Введите первое второе: ")
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)


# n = input("Введите первое число: ")  # '5'
# m = input("Введите первое второе: ")  # 'два'
#
# try:
#     n = int(n)  # 5
#     m = int(m)  # не можем сохранить в число!
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)


# # Цикл while
# i = 0  # Переменная счётчик
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# Итерация - один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# print()
# i = 1
# while i <= 20:
#     print(i + 1, end=" ")
#     i += 2

# n = int(input("Введите количество символов: "))
# print("*" * n)
#
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# a = int(input("Введите начало диапазона: "))  # 1
# b = int(input("Введите конец диапазона: "))  # 2
# res = 0
#
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print("Сумма нечётных элементов: ", res)



# n = input("Введите целое число: ")
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1  # Нужен чтобы цикл не прервался !
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершён!")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1


# while True:  # Когда не знаем сколько раз пользователь захочет ввести!
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break



# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     # else:
#     res *= n
#
# print("Результат:", res)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# Таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#
#         j += 1
#     print()
#     i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1



# i = 0
# while i < 5:  # За строки
#     j = 0
#     while j < 16:
#         if j % 2 == 0:  # За столбцы
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:  # 0
#     j = 0
#     while j < i:  # 0 < 0
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i, "*", sep="")
#     i += 1

# n = int(input("Введи: "))
# m = input("Символ: ")
# с = int(input("0 или 1"))

# range(start, stop, step)
# for i in range(1, 10, 2):  # Шаг только можно увеличивать или вычитать!
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i += 2  # Можно как делить, так и умножать!

# Задача!
# n = int(input("Введите число: "))
# for i in range(1, n + 1):
#     if n % i == 0:
#         print(i, end=" ")


# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:  # Остаток и целочисленное деление
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break  # else - не отработает,
# else:
#     print("Конец!")


# for i in range(3):
#     if i == 1:
#         continue  # else -  отработает,
#     print(i)
# else:
#     print("Конец!")

# вложенные циклы

# for i in range(3):  # 0 1 2
#     print("+++")
#     for j in range(2):  # 0 1
#         print("----")

# l = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(l):
#         if i == 0 or i == h - 1 or j == 0 or j == l - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# st = [i * 2 for i in "Hello"]
# print(st)
#
# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Список (list)
# num = [14, 16, 18, 20, 22, 24, 26, 28, "Hello", True, 2.8]
# print(num)
# print(type(num))
# print(num[0])  # Первое значение
# print(num[-1])  # Последнее значение
# num[0] = 256  # Изменение элемента
# print(num)
# num[1] += 100
# print(num)

# print(len(num))
# print(num[-1])
# print(num[10])
# Создание списка
# s = []
# print(s, type(s))
#
# s2 = list("Python")  # Функция явного преобразования типа
# print(s2, type(s2))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + s2
# print(s3)
# print(s3 * 2)

# Создание списка от 0 - 9
# n = list(range(10))
# print(n)
#
# n = list(range(10, 2, -2))
# print(n)


# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)  # [0, 0, 0, 0, 0]
#
# n = 5
# a = [i + 2 for i in range(n + 1)]
# print(a)  # [0, 1, 2, 3, 4]

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("->"))
# print(a)

# a = [int(input("->")) for i in range(int(input("Введите кол-во элементов списка: ")))]
# print(a)

# lst = [5, 9, 8, 2, 3]
#
# for i in range(len(lst)):  # 0 1 2 3 4
#     print(lst[i], end=" ")
#
# print()
#
# for i in lst:
#     print(i, end=" ")

# a = [int(input("->")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов:", s)

# a = [int(input("->")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print("Сумма отрицательных элементов:", s)

# n = [i + 1 for i in range(20, 40)]
# print(n)

# n = list(range(21, 41))
# print("Список", n)
# s = 0
# k = 0
# for i in range(len(n)):
#     if n[i] % 2:
#         s += n[i]
#     else:
#         k += 1
# print("Сумма нечётных элементов:", s)
# print("Количество чётных элементов:", s)

# a = [int(input("->")) for i in range(int(input("n: ")))]
# print(a)
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print(dir(list))

# Методы списков
# s = [5, 20, 120, 0, 0, 7, 1, 8, 200]
# print(s)
# s.append(99)  # добавляет в конец
# print(s)
# s.extend([1, 2, 3])  # добавляет СПИСОК в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент в список по заданному интервалу
# print(s)

# lst = []  # [3, 1, 7, 8, 9]
# n = int(input("Введите Кол-во эл-ов списка: "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     lst.insert(0, x)
# print(lst)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 7, 3, 2]
# c = []  # [2, 1, 4, 3]

# for i in a:  # 5 # Пока i - находится в списке c
#     for j in b:  # 4
#         if i in c:  # Если i - находится в списке c
#             continue  # Прервёт выполнение текущей итерации - не доходим до append!
#         if i == j:
#             c.append(i)
#             break  # Влияет только на вложенный цикл
# print(c)



# a = [5, 9, 2, 1, 4, 3, 4, 2]
# b = [4, 2, 1, 7, 3, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)  # Дубликаты никакой роли играть не будут!
#
# print(c)


# Задача!
# a = [1, 2, 3]
# b = [11, 22, 33, 4, 5]
# c = []
# if len(b) > len(a):
#     for i in range(len(a)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0 1 2
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)


#
# s = [5, 20, 120, 200, 120]
# print(s)
# s[1:3] = []  # Удаление элементов
# del s[0]  # Удаление элементов
# del s[1:3]
# s.remove(120)  # удаляет элемент из списка по значению (первое вхождение)
# num = 3
# if num in s:
#     s.remove(num)
# print(s)

# s.pop()  # Удаляет последний элемент из списка!
# print(s)

# ind = 3
# try:
#     num = s.pop(ind)  # Удаляем по индексу
#     print(num)
# except IndexError:
#     print(ind, "- Такого индекса не существует!")
# print(s)

# s.clear()
# print(s)

# print("Введите элементы списка: ")
# a = [int(input("->")) for i in range(int(input("n: ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# try:
#     a.pop(k)
# except IndexError:
#     print("Элемент удалить не удалось.", k, "- Такого индекса не существует!")
# print(a)

# s = [5, 20, 120, 200, 120]
# print(s)
#
# num = s.count(120)  # Количество вхождений элемента 120!
# print(num)
#
# ind = s.index(120, 3)  # Вернёт индекс первого вхождения заданного значения
# print(ind)

# a = [1, 2, 3]
# b = a.copy()  # Создаётся дубликат, который располагается по другому id
# print("a =", a)
# print("b =", b)
#
# a.append(20)
# print("a =", a)
# print("b =", b)
#
# b.append(200)
# print("a =", a)
# print("b =", b)

# b = [1, 4, 2, 200]
# print(b)
# # b.reverse()
# b.sort(reverse=True)  # По возрастанию/убыванию
# print(b)
#
# s = ["Виталий", "Сергей", "Анна"]
# print(s)
# s.sort(key=len, reverse=True)  # Сортировака по длине !
# print(s)
#
# c = [51, 32, 3, 200]
# print(c)
# lst = sorted(c, reverse=True)  # Можем сохранить в какую-либо переменную!
# print(c)
# print(lst)

# Генерация случайных чисел

# import random
# # print(dir(random))
#
# print(random.random())  # от 0 - 1
# print(random.randint(0, 9))
# print(random.randrange(9))  # Максимальное число - 8
# print(random.randrange(2, 9, 2))
# print(round(random.uniform(10.5, 25.5), 2))  # Округление до 2 чисел после запятой!

# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# i = 1
# s = [i for i in range(17)]
# print(random.choice(city))
# print(random.choice(s))
#
# print(random.choices(city, k=3))  # Сл чис опред колич
# print(random.choices(s, k=3))
#
#
# random.shuffle(city)  # В неопределённом порядке
# print(city)
# random.shuffle(s)
# print(s)

# mas = [random.randint(20, 40) for i in range(10)]
# print(mas)

# lst = [38, 23, 27, 35, 26, 39, 21, 22, 28, 24]
# print(lst)
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
#
# print(city)
# print(len(city))
# print(min(city))  # По коду символа
# print(max(city))


import random
import re
from gc import get_count


# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# max_1 = max(lst)
# print("max =", max_1)
# lst.remove(max_1)
# lst.insert(0, max_1)
# print(lst)

# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
# min_1 = min(lst)
# print("min =", min_1)
# ind = lst.index(min_1)
# print("Index =", ind)
#
# del lst[0:ind]
# print(lst)

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)

# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
#
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Третий список:", c)

# c = [min(a), min(b), max(a), max(b)]
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# # print(m[2][2])
# #
# # st = ["Hello", "World"]
# # print(st[1][4])
# print("Вариант 1")
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
#
# print("Вариант 2")
# for i in m:
#     # print(i)
#     for j in i:
#         print(j, end="\t")
#     print()

# Modules

# import math
#
# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# import math as m  # Псевдоним
#
# num1 = m.sqrt(2)
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import sqrt, ceil, floor  # Только заданные функции, самый маленький вес!
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import *  # Импортируем всё! Размер документа полностью!
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import pi
#
# # print(pi)
#
# r = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2*pi*r, 2))

# import time
# import locale

# print(time.time())  # Начало цифрового времени
# print(time.ctime())  # Сегодняшняя дата / преобразовывает количество секунд по заданному формату
# print(time.localtime())  # Как ключи и значения:
# res = time.localtime()
# print(res.tm_year)
#
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(55555345)))
# print(time.strftime("Today: %B %d, %Y."))
#
# locale.setlocale(locale.LC_ALL, "ru")  # Применяется локализация ко всему! Русский язык
# print(time.strftime("Сегодня: %B %d, %Y."))  # Шаблон! Полное название месяца День месяца Год(полное число)
#
# num = 1_000_000.0
# print(num)  # 1*000*000.0

# pause = 1.5
# print("Программа запущена")
# time.sleep(pause)  # Программа завершится через указанные секунды
# print(pause, "seconds")


# start = time.time()  # Засечь время!
# time.sleep(5)
# finish = time.time() - start
# print(finish)


# Function После функции и до функции - две пустые линии
# print()
#
#
# def hello(name, age):
#     print("меня зовут:", name, "мне", age, "лет")
#
#
# hello("Irina", 20)
# hello(18, "Vlad")


# def get_sum(a, b):
#     print("Сумма чисел: ", end="")
#     return a + b  # Возвращается туда - куда вызывается функция!


# x = 3
# y = 6
# get_sum(x, y)
# get_sum("abc", "def")

# res = get_sum(2, 5)
# print(res)

# Задача!
# def change(lst):
#     # 1-й Способ
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     # return lst
#     # 2-ой Способ
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def test(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# # print(test(10, 5))
# # print(test(5, 10))
# num1 = 10
# num2 = 23
# if test(num1, num2):
#     print(num1, ">", num2)
# else:
#     print(num1, "<", num2)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     for i in password:
#         if "A" <= i <= "Z":
#             has_upper = True
#         if "a" <= i <= "z":
#             has_lower = True
#         if "0" <= i <= "9":
#             has_number = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")


# def get_sum(a, b, c=0, d=1):  # Позиционные параметры
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 3, 4))
# print(get_sum(1, 2, 3))
# print(get_sum(1, 2, d=3))

# def display_info(name, age):
#     print("Name", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info("Igor", age=23)  # Именованные параметры

# a = "Hello"
# b = "Hello"
# print(a, id(a))
# print(b, id(b))
# print(a == b)
# print(a is b)  # is - ссылается ли переменные на одну и туже ячейку в памяти?
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)

# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))
# lt1.pop(1)
# print(lt1, id(lt1))

# s = "Hello"
# print(s, id(s))
# # s = s + "!"  # Перезаписываем переменную!
# s += "!"
# print(s, id(s))

# a = 5
# print(a, id(a))
# a = a + 0
# print(a, id(a))

# def test1(lst):
#     lst.append(4)
#
#
# x = [1, 2, 3]
# print(test1(x))
# print(x)
#
#
# def test2(n):
#     n = 5
#
#
# x1 = 3
# print(test2(x1))
# print(x1)

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())  # Показывает размер!
# print(tpl.__sizeof__())  # Экономит память!

# print(lst[1])
# print(tpl[1])
#
# lst[1] = 50
# # tpl[1] = 10 - Не поддерживает данное действие! (неизменяемый тип !)

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}  # Является множество - частью другого множества?
# print(a >= b)  # True - b является подмножеством a
# print(a <= b)


# a = {3, 1, 4, 2, 0}  # В порядке
# print(a, type(a))
# lst = list(a)  # По своей структуре похожи друг на друга
# print(lst, type(lst))
# # lst = tuple(a)
# # print(lst, type(lst))
# b = set(lst)
# print(b, type(b))


# s = frozenset("hello")  # Используется в основном для хранения данных
# print(s)
#
# s = frozenset(["hello", "world"])
# print(s)
#
# a = frozenset({i ** 2 for i in range(10)})
# print(a)

# Словарь (dict)
# lst = [1, 2, 3]
# d = {"one": 1, "two": 2, "three": 3}  # Словарь (изменяемый тип данных)
# print(lst, type(lst))
# print(d, type(d))
# print(lst[1])
# print(d["two"])
# d["two"] = 200
# print(d)

# d = {"one": 1, "two": 2}
# print(d, type(d))
#
# d1 = dict(one=1, two=2)  # Явное преобразование
# print(d1, type(d1))


# def func(one, two):
#     return one, two
#
#
# print(func(two=1, one=2))

# lst = [["one", 1], ["two", 2], ["three", 3]]
#
# print(lst)
# print(dict(lst))

# d = {0: "text", True: 1, (1, 2): "кортеж", "список": [5, 6, 6], 1: 10, False: 0}  # Ключами могут быть только неизменяемые типы данных! Значение - любой тип данных Уникальность распространяется на ключи
# print(d)

# d = {i * 2: i ** 2 for i in range(7)}
# print(d)

# d = {input("->"): input("->") for i in range(7)}
# print(d)

# from random import randint
# d = {randint(1, 10): input("->") for i in range(7)}
# print(d)


# d = {0: "text", True: 1, (1, 2): "кортеж", "список": [5, 6, 6], 1: 10, False: 0}
# print(d["список"][1])
# print(d[(1, 2)])
# print(d[0])  # Ключ!


# d = {"one": 1, "two": 2}  # Есть ли ключ в словаре?
# # print("one" in d)
# # print(2 in d)
# key = "two"
# try:
#     print(d[key])
# except KeyError:
#     print("Элемента с ключом", key, "нет в словаре")
# del d["two"] # Удаление значения из словаря (ключ без значения - существовать не может!)
# print(d)

# for key in d:
#     print(key, d[key])

# try:
#     n = int(input("Количество овощей: "))
#     sp = {i+1: input("-> ") for i in range(n)}
#     print(sp)
#     q = int(input("Какой элемент исключить: "))
#     del sp[q]
#     print(sp)
# except KeyError:
#     print("Нет такого ключа!")

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# q = int(input("Какой элемент исключить: "))
# del d[q]
# print(d)

# d = {"one": 1, "two": 2}
# print(d)
# print(len(d))

# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core i5-4570K", 4, 2000],
#     "3": ["AMD FX--6300", 3, 4500],
#     "4": ["Core-i3-4330", 9, 3000],
#     "5": ["Core-i3-4330", 9, 4500],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != "0":
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     while True:
#                         if count > 0:
#                             goods[n][1] += count
#                             break
#                         else:
#                             print("Количество должно быть положительным числом")
#                             count = int(input("Количество: "))
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует!")
#     else:
#         break
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")

# print(dir(dict))
# d = {"one": 1, "two": 2, "three": 3}  # Методы!

# print(d.keys())  # Список ключей
#
# print(d.values())  # -\\- Значений
#
# print(d.items())  # -\\- Всё
#
# print(tuple(d.keys()))
# print(tuple(d.values()))
# print(tuple(d.items()))

# for i, j in d.items():  # Список кортежей !
#     print(i, ":", j)

# d = {"one": 1, "two": 2, "three": 3}
# d2 = d.copy()  # Все изменения присутствуют только в изменяемом словаре !
# print("D =", d)
# print("D2 =", d2)
# d2["two"] = 200
# print("D =", d)
# print("D2 =", d2)
# d["four"] = 4
# print("D =", d)
# print("D2 =", d2)


# d = {"one": 1, "two": 2, "three": 3}
# # print(d["three1"])  # KeyError
# # value = d.get("three2", "Такого элемента в словаре нет!") # проверка на наличие данного ключа! None - если нет его!
# # value = d.get("three2", False)  # Если обращение даёт исключение - возвращает указанное значение
# # value = d.pop("two1", "Такого ключа не существует!")  # Удаление значения
# # item = d.popitem()  # По умолчанию удаляет последний элемент
# # print(item)
# # d.clear()  # Очищает элементы из словаря!
# # item = d.setdefault("two2", 4)
# # print(item)
# print(d)
# # d2 = {"four": 4, "five": 5}
# d2 = [("four", 4), ("five", 5)]  # Список кортежей м.б. преобразован в словарь
# print(d2)
# # d3 = d | d2  # Сложение
# # print(d3)
#
# d.update((d2))  # Более универсальный метод добавления
# print(d)

# d = {"name": "Kell", "age": 25, "salary": 8000, "city": "New Your"}
#
# new_d = dict()
# new_d["name"] = d.pop("name")
# new_d["salary"] = d.pop("salary")
#
# print(d)
# print(new_d)
  # Область видимости
# def add(a):
#     x = 2
#
#     def inner():
#         print("x =", x)
#         return a + x
#     return inner()
#
#
# print(add(3))

# def outer(who):
#     def inner():
#         print("Hello", who)
#     inner()
#
#
# outer("World")


# def outer():
#     a = 6  # Одна пустая линия перед вложенной функцией! # 2
#
#     def inner(b):
#         a = 4  # 5
#         print("Сумма", a + b)  # 6
#
#     print("a =", a)  # 3
#     inner(5)  # 4
#
#
# outer()  # 1


# x = 25
# t = 0  # Чтобы не было подчёркиваний
#
#
# def fn():
#     global t
#     a = 30   # 35 - Перезаписывает
#
#     def inner():
#         nonlocal a  # Сделать не локальной # Видна из области и перезаписывает а во внешней функции
#         a = 35
#         print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t  # 25 + 30 -> 55 # 25 + 35 -> 60
# print(c)


# def fn1():
#     x = 25  # 2
#
#     def fn2():
#         x = 33  # 55
#         d = x
#
#         def fn3():
#             nonlocal x  # До уровня глобальной переменной дойти не может
#             x = 55
#
#         fn3()  # 5
#         print("fn2.x =", x)  # 33
#         print("d =", d)
#
#     fn2()  # 3
#     print("fn1.x =", x)  # 25
#
#
# fn1()  # 1

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]

# def func1():  # Снаружи - внутрь все переменные видны
#     a = 1  # 2
#     b = "line"  # line!
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         print(a)
#         a = a + 1  # Не изменяемый тип данных!
#         b = b + "!"  # Не изменяемый тип данных!
#         return a, b, c
#
#     return func2()
#
#
# print(func1())


# Замыкание - наружная функция возвращает вложенную без её вызова

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# p1 = outer(4)  # p1 - функция(inner) под другим названием!
# print(p1(10))
#
# p1 = outer(6)
#
#
# print(outer(5)(4))

# def func(city):
#     count = 0
#
#     def inner():
#         nonlocal count
#         count += 1
#         print(city, count)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(5, 6))
# # Анонимные функции (lambda - выражения) - Для вставки служебного элемента
#
# print((lambda x, y: x + y)(1, 2)) # вернуть мы можем только одно действие
#
# fn = lambda x, y: x + y
# print(fn(5, 6))

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# print((lambda a, b, c: a + b + c)(1, 2, 3))
# print((lambda a, b, c=3: a + b + c)(1, 2))  # Значение по умолчанию
# print((lambda a, b, c=3: a + b + c)(b=1, a=2))
#
# print((lambda *args: sum(args))(1, 2, 3, 4))


# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for t in c:
#     print(t("abc__"))


# def outer(n):
#
#     def inner(x):
#         return n + x
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer(n):
#     return lambda x: n + x  # lambda - может быть написана в той же строке
#
#
# f = outer(5)
# print(f(10))
#
#
# outer = lambda n: lambda x: n + x
# f = outer(5)
# print(f(10))
#
#
# print((lambda n: lambda x: n + x)(5)(10))

# def sort_list(i):
#     return i[1]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}
# print(d)
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=sort_list)  # НЕТ скобок - потому что в i приходит каждый кортеж
# print(dict(lst))


# Задача1
#
# players = [
#     {"name": "Антон", "last name": "Бирюков", "rating": 9},
#     {"name": "Алексей", "last name": "Бодня", "rating": 10},
#     {"name": "Федор", "last name": "Сидоров", "rating": 4},
#     {"name": "Михаил", "last name": "Семенов", "rating": 5}
# ]
#
# print(sorted(players, key=lambda item: item["last name"]))  # Сортировка по ключу last name
# print(sorted(players, key=lambda item: item["rating"], reverse=True))  # Разворачивает элементы в противоположную сторону
# print(sorted(players, key=lambda item: item["rating"]))


# lst = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(lst[0](10, 5))
# print(lst[2](10, 5))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("вторник"),
#     3: lambda: print("среда"),
#     4: lambda: print("четверг"),
#     5: lambda: print("пятница"),
#     6: lambda: print("суббота"),
#     7: lambda: print("воскресенье"),
# }
#
# d[7]()  # Вызов lambda функции через - ()

# print((lambda a, b: a if a > b else b)(15, 7))
#
# map(func, *iterable), filter(func, *iterable)

# Первый способ
# def mult(t):
#     return t * 2
#
#
# lst = [2, 6, 7, 8, -10]
#
# print(list(map(mult, lst)))  # Проходится по каждому элементу итерированного обьекта и умножает на 2 Нужно явно указать тип данных!
# # Второй способ
# print(list(map(lambda t: t * 2, lst)))

# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# st = ['a', 'b', 'c']
# num = [1, 2, 3, 5]  # Отбрасывает лишние элементы
# val = [2.0, 5.4, 7.8, 9.4, 7.4]
# print(list(map(lambda x, y, z: (x, y, z), st, num, val)))
# print(dict(map(lambda x, y: (x, y), st, num)))

# ЗАНЯТИЕ 11
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# new_list = list(map(lambda x, y: x + y, l1, l2))
# print(new_list)

# t = ("abcd", "abc", "adefg", "def", "ghi")
#
# t2 = tuple(filter(lambda s: len(s), t))
# print(t2)

# b = [66, 99, 68, 59, 76, 60, 88, 74 , 81, 68]
# # res = list(filter(lambda s: s > 75, b))  # Фильтрация(Сортировка) всех элементов по какому-то условию
# res = list(filter(lambda s: s > sum(b) / len(b), b))
# print(res)


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))  # 1-й Способ!
#
# print(list(range(1, 10)))
# print(list(filter(lambda x: x % 2, range(1, 10))))
# print(list(map(lambda x: x ** 2, [1, 3, 5, 7, 9])))
#
# print([x ** 2 for x in range(1, 10) if x % 2])  # 2-й Способ


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_hello'")
#     print(func())  # Любая функция может принимать параметром другую функцию
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# test = hello  # Функции присваиваем любые другие переменные без скобок!
# print(type(test))
# print(test())


# def my_decorator(func):
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'hello'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # Декорирующая функция
#     def inner():
#         print("Код до вызова функции")
#         func()
#         print("Код после вызова функции")
#     return inner
#
#
# @my_decorator  # Декоратор (Добавляет дополнительный код неявным образом) -> функция проходит через декоратор
# def func_test():  # Декорируемая функция
#     print("Hello, I am func 'hello'")
#
#
# @my_decorator
# def hello():
#     print("Hello, I am func 'hello'")
#
#
# func_test()
# print()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def outer(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")

# def outer(fn):
#     def wrap(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @outer
# def print_students(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_students("Борис", "Елизавета", "Светлана", study="JS")
# print_students("Борис", "Елизавета", "Светлана")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")  # Добавление параметров
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def decor1(arg):
#     def decor2(fn):
#         def wrap(*args, **kwargs):
#             return arg * fn(*args, **kwargs)
#
#         return wrap
#     return decor2


# @decor1(3)
# def mn(a):
#     return a
#
#
# print(mn(2))
# def typed(*args, **kwargs):
#     def wrap(fn):
#         def wrap2(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#         return wrap2
#     return wrap
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# print(typed_fn(3, 4, "Python"))


# ЗАНЯТИЕ 12
# name = "Дмитрий"
# age = 25
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="")
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print(f"{x} x {y} / 2 = {x * y / 2}")
# print(f"{round(45.456778, 2)}")
# print(f"{45.456778:.0f}")  # 0 - количество символов f - в вещественной части

# num = 74
# print(f"{{num}}")  # Как в виде строки
# print(f"{{{num}}}")

# dir_name = "folder"
# file_name = "file.py"
# print(fr"home\{dir_name}\{file_name}")  # r - символ \ f - переменная
# print("home\\" + dir_name + "\\" + file_name)
# print("home\\", dir_name, "\\", file_name, sep="")


# s1 = ('Многострочный \n'
#       'текст')
# print(s1)
#
# s = """Многострочный
#     текст
#     read"""  # Форматируется так как мы его указали!
# print(s)
#
# s2 = ''''Многострочный
#     текст
#     read'''  # Форматируется так как мы его указали!
# print(s)

# """
# Многострочный
# комментарий
# """  # Не является комментарием! Будет воспринимать как текст без обьявления в переменную
#
# "Многострочный"
# "комментарий"

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(len.__doc__)

# print(min([1, 2, 3]))
# print(len([1, 2, 3]))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('Ц'))

# print("a" > "#")

# while True:
#     n = input("-> ")
#     if n == "-1":
#         break
#     else:
#         print(ord(n))

# my_str = "Test string for me "
# arr = [ord(x) for x in my_str]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr  # Округление до целого! + добавление списка
# print(arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]  # Первые три элемента строки!
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)  # Сортировка по убыванию
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# from random import randint
#
# shortest = 6
# longest = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     random_length = randint(shortest, longest)  # Включая longest!
#     res = ""
#     for i in range(random_length):
#         res += chr(randint(min_ascii, max_ascii))
#     return res


# print("Ваш случайный пароль:", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.

# print(s.lower().count("l"))
# print(s.count('h', 1, -4))  # Поиск с первого индекса

# print(s.find("Python"))  # Возвращает индекс искомой подстроки, если совпадений нет, то -1
# print(s.find("l"))
# print(s.find("l", 4, 19))
#
# print(s.index("Python4"))  # Возвращает индекс искомой подстроки, если совпадений нет, то выбрасывает исключение
# ValueError


# st = "один два"
# first = st[:st.find(" ")]
# second = st[st.find(" ") + 1:]
# print(second + " " + first)

# s = "hello, WORLD! I am learning Python."
# print(s.find("l"))
# print(s.rfind("l"))
# print(s.rindex("l"))

# print(s.endswith("on."))
# print(s.endswith("LD!", 10, 13))
# print(s.index("LD!"))

# print(s.startswith("hel"))
# print(s.startswith("I am", 14))
# print(s.index("I am"))

# print("abc123".isalnum())  # Определяет состоит ли строка из букв и цифр
# print("abc1!!!23".isalnum())
# print("ABCabc".isalpha())
#
# print("23".isdigit())
# print("abc".islower())
# print("abc123!".islower())
#
# print("ABC".isupper())


# print("py".center(10, "-"))

# print("        py".lstrip())
# print("        py       ".strip())

# print("https://www.python.orgw".lstrip("/:psth").rstrip(".orgw"))
# print("https://www.python.orgw".strip("/:psth.orgw"))

# s = "hello, Python! I am learning Python. Мне нравится Python."
# print(s.replace("Python", "JS", 2))  # Замена в количестве двух раз

# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("...".join(['1', '99']))
# print(":".join("Hello"))

# ЗАНЯТИЕ
# print("Строка разделённая пробелами".split())
# print("www.python.org.ru".split(".", 2))  # Два разделения !

# fio = input("Введите ФИО: ").split()
# print(f"{fio[0]} {fio[1][0]}. {fio[2][0]}.")

# lst = input("Введите числа через пробел: ").split()
# print(lst)
# lst = map(int, lst)
# print(sum(lst))
#
# import re

# s = "Я ищу совпадения в 2025 году. \"И я их найду в 2 счё-та\". H.ello_World."
# # reg = "\\."  # Экранирование точки
# # reg = r"\."  # Экранирование точки
# # reg = r"[оя]"
# # reg = r"[оя]"
# reg = r"^\w+\s\w+"  #  Поиск от начала
# reg = r"\w+\.$"  # Поиск в конце
# print(re.f
# indall(reg, s))
# # print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# # print(re.search(reg, s))  # <re.Match object; span=(15, 16), match='я'> Месторасположения первого совпадения с шаблоном
# # print(re.search(reg, s).span())  # (15, 16) - Может выдать ошибку
# # print(re.search(reg, s).start())  # 15
# # print(re.search(reg, s).end())  # 16
# # print(re.search(reg, s).group())  # я
# #
# # print(re.match(reg, s))  # Ищет совпадение от начало строки, Месторасположения первого совпадения с шаблоном в нач строк
# # print(re.split(reg, s))  # возвращает список в котором строка разбита по шаблону
# # print(re.sub(reg, "!", s, 1))  # Замена точки на ! Поиск и замена
# #
# # reg = r"[205]"
# # reg = r"[12][0-9][0-9][0-9]"
# reg = r"[A-Za-z.]"
# reg = r"[A-Z\[a-z\].-]"
# reg = r"[^0-9]"
# reg = r"\AЯ ищу"
# reg = r"\w+"
# reg = r"20*"
# # print(re.findall(reg, s))
#
#
# # st = "Час в 24-часовом формате от 00 до 23. 2021T21:45. Минуты, в диапазоне от 00 до 59. 2021-06015T01:09"
# # reg1 = "[0-2][0-9]:[0-5][0-9]"
# # print(re.findall(reg1, st))
#
# print(re.findall(reg, s))

# d = "Цифры: 79, +12, -435, 0.013"
# # print(re.findall(r"[+-]?\d+\.?\d*", d))
# print(re.findall(r"[+-]?\d+[.?\d]*", d))

# d = "05-03-1987"
#
# print("Дата рождения:", re.sub(r"\s#.*","", d))

# st = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+[\s\w.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
# print(re.split(r";\s+", st))

# s1 = "12 сентября 2025 года 545435344"
# # reg1 = r"\d{2,4}?"  # reg1 = r"\d{2}"
# # reg1 = r"\d{2}"
# reg1 = r"\d{,4}"
# # # reg1 = r"\d{2,}"
# # reg1 = r"\d{4}"
# print(re.findall(reg1, s1))

# st = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg1 = r"\+?7\d{10}"
# print(re.findall(reg1, st))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("masfdfd"))

# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))


# text = "hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# reg = r"я"  # Поиск в конце
# print(re.findall(reg, s, re.IGNORECASE))
#
# text = """
# one
# two
# """

# print(re.findall(r"one.\w+", text))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))

# print(re.findall("""[a-z.-]+
#  @
#  [a-z.-]  # part1
#  +        # part2
#  """, "test@mail.com", re.VERBOSE))  # Игнорирует комментарий


# text = """Python,
# python,
# PYTHON
# """
#
# reg1 = "(?im)^python"
# print(re.findall(reg1, text))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))


# *?, +?, ??+
# {m,n}?, {,n}?, {m,}?

# Занятие 15

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий|Виктор"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# reg = r"\w+\s*=\s*\d[.\w+]*"
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"
# print(re.search(reg, s).groups())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])  # Номер первой круглой скобке (наружная)
# print(m[2])  # -||- вторая круглая скобка
# print(m[3])  # -||- третья круглая скобка
#
# # print(re.findall(reg, s))


# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))

# a = "31-01-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9]"  # [12] - или 1 или 2
# print(re.findall(pattern, a))

# s = "Самолёт прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# Рекурсия


# def elevator(n):  # 5, 4, 3, 2, 1, 0
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevator(n - 1)  # стек: 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = 5
# elevator(n1)


# Занятие 16


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список файлов")
# f.close()
#
# f = open("text2.txt", "r")
# read_line = f.readlines()
# print(read_line)
# read_line[1] = "Hello World\n"
# print(read_line)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_line)
# f.close()

# f = open("test.txt")
# print(f.read(3))
# print(f.tell())  # Возвращает условную позицию текущего курсора в файле
# print(f.seek(1))  # Перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("test3.txt", "w")
# # print(f.write("I am learning Python"))
# # print(f.seek(3))
# # print(f.write("-new string-"))
# # print(f.tell())
# f.close()


# with open("test3.txt", "w+") as f:
#     print(f.write("0123456"))
# print(f.closed)


# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open("test3.txt", "w") as f:
#     f.write(get_line(lst))
#
# print("Файл создан")

# with open("test3.txt", "r") as f:
#     num = f.read()
#
# print(num)
# num_list = list(map(float, num.split()))
# print(num_list)
# res = 1
# for i in num_list:
#     res *= i
# print(res)


# file_name = "test3.txt"
#
# with open(file_name, "w") as f:
#     f.write("Файл именованная область данных на носителе информации, используемая как базовый объект"
#             " взаимодействия с данными в операционных системах.")  #
#
#
# def longest_words(file):
#     with open(file, "r") as text:
#         w = text.read().split()
#         print(w)
#         res = len(max(w, key=len))  # Сортировка элементов по алфавиту (с помощью key! найдем искомое слово)
#         lst = [word for word in w if len(word) == res]
#         if len(lst) == 1:
#             return lst[0]
#         return lst
#
#
# print(longest_words(file_name))

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("one.txt", "w") as f:
#     f.write(text)


# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

# Модуль OS и OS.PATH

# import os

# print(os.getcwd())
# print(os.listdir("folder"))
# os.mkdir("folder1")
# os.makedirs("nested1/nested2/nested3")
# os.rmdir("folder1")
# os.remove("test.txt")
# os.rename("two.txt", "folder/two_new_1.txt")

# for root, dirs, files in os.walk("nested1"):
#     print("Root:", root)
#     print("\tDirs:", dirs)
#     print("\tFiles:", files)


# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk("nested1"):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена")
#     print("-" * 50)
#
#
# remove_empty_dirs("nested1")

# import os
# import os.path

# print(os.path.split(r"nested1/nested2/nested3/test3.txt"))
# print(os.path.join("D:\\", "nested1", "nested2", "nested3", "test3.txt"))
# print(os.path.join( "nested2", "D:\\", "nested1", "nested3", "test3.txt"))
# print(os.path.isdir(r"nested1/nested2/nested3/test3.txt"))  # Путь из файла
# print(os.path.isfile(r"nested1/nested2/nested3/test3.txt"))  # К файлу


# import os.path


# dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)

# files = {
#     r"Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
#
# files_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in files_with_text:
#     with open(file, "w") as f:
#         f.write(f"Какой-то текст в файле {file}")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {"сверху вниз" if topdown else "снизу вверх"}")
#     for root, dirs, my_files in os.walk(root, topdown):
#         print(root)
#         print(dirs)
#         print(my_files)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)


# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# import os
# import time
#
# path = r"main.py"
#
# kb = os.path.getsize(path)  # Размер документа (В байтах)
#
# print(kb // 1024)  # В Кбайтах
#
# kb = os.path.getsize(path)
#
# atime = os.path.getatime(path)  # Дата последнего доступа к документу
#
# ctime = os.path.getctime(path)  # Время создания файла (последнего изменения файла)
#
# mtime = os.path.getmtime(path)  # Время последнего изменения файла
#
# print(atime)
# print(ctime)
# print(mtime)
#
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(ctime)))
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# ООП

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 2
#
#     def set_coords(self, x1, y1):
#         self.x = x1
#         self.y = y1
#         print(self.__dict__)
#
#
# p1 = Point()  # Экземпляр класса
# p1.x = 100
# p1.y = 200
# # print(p1.x, p1.y)
# # print(p1.__dict__)  # Возвращает в виде словаря набор элементов класса (Покажет значения, поскольку переменные
# # были переопределены)
#
# p2 = Point()
# # print(p2.x, p2.y)
# # print(p2.__dict__)
# #
# # print(Point.__dict__)
# # print(Point.__doc__)
# Point.set_coords(p1, 111, 112)  # Способ вызова метода
#
# p1.set_coords(8, 200)
# p2.set_coords(10, 20)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}"
#               f"\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, name1, birthday1, phone1, country1, city1, address1):
#         self.name = name1
#         self.birthday = birthday1
#         self.phone = phone1
#         self.country = country1
#         self.city = city1
#         self.address = address1
#
#     def set_name(self, name):  # Устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # Получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
# h1.print_info()
# h1.set_name("Алексей")
# print(h1.get_name())

# class Person:
#     skill = 10  # Статическое свойство
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name  # Динамические свойства (перезаписываются)
#         self.surname = surname
#         print("Инициализация")
#
#     def __del__(self):  # Разрыв ссылки на экземпляр
#         print("Финализатор (Деструктор)")
#
#     def print_info(self):
#         print("\nДанные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1  # Счётчик создания классов
#         # self.count += 1
#
#
# p1 = Point(1, 2)
# print(Point.count)
# p2 = Point(10, 20)
# print(Point.count)
# p3 = Point(100, 200)
# print(Point.count)
# print(p1.count)
# print(p2.count)

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# class Robot:
#     k = 0
#
#     def __init__(self, name):  # Может располагаться где угодно в классе
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "Выключается!")
#         Robot.k -= 1
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#         if Robot.k == 0:
#             print(self.name, "Был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
#
# droid3 = Robot("C-4PO")
# droid3.say_hi()
#
# print("Численность роботов:", Robot.k)
#
# print("\nРоботы могут проделать какую-либо работу.\n")
#
# print("Завершили работу")
#
# del droid1
# del droid2
# del droid3
# print("Численность роботов:", Robot.k)

# class Point:
#     __slots__ = "__x", "__y"  # Разрешили что свойства будут внутри класса
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check(x) and Point.__check(y):
#             self.__x = x
#             self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check(c):
#         return isinstance(c, (int, float))
#
#     def set_coord(self, x, y):
#         if isinstance(x, int) or isinstance(x, float) and isinstance(y, int) or isinstance(y, float):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# # p1.z = 3  # Добавлять свойства!
# # print(p1.z)
# # p1.__x = "abc"  # Создаём новые два свойства
# # p1.__y = "abc"
# # print(p1.__dict__)
# # print(p1.__x, p1.__y)
# print(p1.get_coord())
#
# p1._Point__x = 111
# print(p1.__dict__)


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов __set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# print(p1.x)
# p1.x = 50
# print(p1.x)
# del p1.x


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property  # геттер
#     def x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     @x.setter  # сеттер
#     def x(self, x):
#         if isinstance(x, int):
#             self.__x = x
#         else:
#             print("Не корректный тип данных")
#
#     # @x.deleter
#     # def x(self):
#     #     print("Удаление свойства")
#     #     del self.__x
#
#     # x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# # print(p1.x)
# p1.x = "50"
# print(p1.x)
# # del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg  # _KgToPounds__kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами!")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = 41
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = "Десять"


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name1):
#         if isinstance(name1, str):
#             self.__name = name1
#         else:
#             print("Не строка!")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age1):
#         if isinstance(age1, int):
#             self.__age = age1
#         else:
#             print("Не число!")
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# person = Person("Irina", 26)
# print(person.__dict__)
# person.name = "Igor"
# print(person.__dict__)
# person.age = 31
# print(person.__dict__)
# del person.name
# print(person.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.__dict__)
# print(Point.get_count())

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(Point.__dict__)
# print(Point.get_count())

# def inc(x):
#     return x + 1
#
#
# def dec(x):
#     return x - 1
#
#
# print(inc(10), dec(10))

# class Change:
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#     def print_info(self):
#         print("Печать инфо", self.name)
#
#
# print(Change.inc(10), Change.dec(10))

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a  # 3
#         if b > mx:  # 5 > 3
#             mx = b  # 5
#         if c > mx:  # 7 > 5
#             mx = c  # 7
#         if d > mx:  # 9 > 7
#             mx = d  # 9
#         return mx
#
#     @staticmethod
#     def min(*args):
#         mn = args[0]
#         for i in args:
#             if i < mn:
#                 mn = i
#         return mn
#
#     @staticmethod
#     def average(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def factorial(n):
#         fact = 1
#         for i in range(1, n + 1):
#             fact *= i
#         return fact
#
#
# print(Numbers.max(3, 5, 7, 9))
# print(Numbers.min(3, 5, 7, 9))
# print(Numbers.average(3, 5, 7, 9))
# print(Numbers.factorial(0))

# "23.10.2025" => 2025-10-23

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def string_to_db(self):
        return f"{self.year}-{self.month}-{self.day}"

    @classmethod
    def from_string(cls, string_date):
        day, month, year = map(int, string_date.split("."))
        date = cls(day, month, year)
        return date

    @staticmethod
    def is_date_valid(string_data):
        if string_data.count(".") == 2:
            day, month, year = map(int, string_data.split("."))
            return day <= 31 and month <= 12 and year <= 3999


dates = [
    "23.10.2025",
    "30-10-2025",
    "01,10,2025",
    "12.10.2025",
]

for i in dates:
    if Date.is_date_valid(i):
        date1 = Date.from_string(i)
        print(date1.string_to_db())
    else:
        print("Не правильная дата или формат строки с датой")


# string_date = "23.10.2025"
# day, month, year = map(int, string_date.split("."))  # [23, 10, 2023]
# # print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())


# date1 = Date.from_string("23.10.2025")
# print(date1.string_to_db())