"""Векторное произведение
Задание: Разработать функцию для вычисления векторного (кросс) произведения двух трёхмерных векторов."""

import numpy as np
def cross_product(v1, v2):
    return np.cross(v1, v2)

# Пример использования
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(cross_product(v1, v2))  # Output: [-3 6 -3]
