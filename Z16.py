# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
# 1 2 3 4 5
# 3 -> 1
import random
N = int(input("Введите количество элементов списка: "))
list_1 = []
for i in range(N):
    list_1.append(i+1)
# for i in range(N):        ##Для массива из случайных чисел
#     list_1.append(random.randint(0, 10))
print(*list_1)
X = int(input("Введите искомый элемент: "))
match = 0
for i in range(len(list_1)):
    if list_1[i] == X:
        match += 1
print(f'Количество повторений искомого элемента в списке: {match}')