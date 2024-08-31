"""Транспонирование матрицы
Цель: Написать функцию, которая принимает матрицу (двумерный массив)
и возвращает её транспонированную версию. 
Убедитесь, что ваша функция может обрабатывать матрицы различной размерности."""

import numpy as np
def transpose_matrix(matrix):
    matrix = np.array(matrix)
    return matrix.T

# Пример использования функции
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))  # Output: [[1 4]
                                                  #          [2 5]
                                                  #          [3 6]]
