# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randrange

random_list=[randrange(1,10) for i in range(20)]
print(random_list)
random_list=set(random_list)
print(random_list)


