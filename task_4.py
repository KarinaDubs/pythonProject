"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
# Вариант 1:

number = list(input("Введи большое число" ))
print(max(number))

# Вариант 2:

a = int(input("Введите целое цисло:"))
m = a//10
print(m)
max_number = a%10
a = a//10
while a > 0:
    if a%10 > max_number:
        max_number = a%10
        a = a//10
print(max_number)
