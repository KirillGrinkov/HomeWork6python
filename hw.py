# # Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('input a :'))
d = int(input('input d :'))
n = int(input('input n :'))
for i in range(n):
    print(a*1 + i * d, end=' ')

# Задача 32: Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

list = []
from random import randint
 
max = int(input('input max :'))
min = int(input('input min :'))

size = int(input('Input size list:'))

list = [randint(1, 10) for _ in range(size)]

print(list)
print()

for i in range(len(list)):
    if min <= list[i] <= max:
        print(i, end=' ')





