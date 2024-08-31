"""Сложение векторов
Цель: Написать функцию для сложения двух векторов."""


import numpy as np

def add_vectors(v1, v2):
    return np.add(v1, v2)

# Пример использования
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(add_vectors(v1, v2))  # Output: [5 7 9]
