"""Векторное произведение
Задание: Разработать функцию для вычисления векторного (кросс) произведения двух трёхмерных векторов."""

import numpy as np
def cross_product(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    return np.cross(v1, v2)

# Пример использования
v1 = [1, 2, 3]
v2 = [4, 5, 6]

v1 = [1, 6]
v2 = [4, 8]


print(cross_product(v1, v2))  # Output: [-3 6 -3]
