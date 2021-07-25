"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
#
a = int(input("Введи еще одно число:", ))
a = str(a)
b = str(a) + str(a)
c = str(a) + str(a) + str(a)
d = int(a) + int(b) + int(c)
print(d)


a = int(input("Введи число:", ))
b = str(a) + str(a)
c = str(a) + b
d = a + int(b) + int(c)
print(d)

a = input("Введи число:")
b = int(a) + int(2*a)+int(3*a)
print(b)
