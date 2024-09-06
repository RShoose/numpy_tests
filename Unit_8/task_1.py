"""Сложение векторов
Задание: Написать функцию для сложения двух векторов."""


import numpy as np

def add_vectors(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.add(v1, v2)

# Пример использования
v1 = [1, 2, 3]
v2 = [4, 5, 6]

v1 = [1, 2, 3, 6, 7]
v2 = [4, 5, 6, 9, 10]
print(add_vectors(v1, v2))  # Output: [5 7 9]
