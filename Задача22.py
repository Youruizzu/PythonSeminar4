# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))
array1 = []
array2 = []

for i in range(0, n):
    array1.append(random.randint(1, 99))
for i in range(0, m):
    array2.append(random.randint(1, 99))

array3 = array1 + array2

numset = sorted(set(array3))

print(*numset)