"""Решение системы линейных уравнений
Задание: Использовать функцию `numpy.linalg.solve` для решения системы линейных уравнений."""

import numpy as np
def solve_linear_system(A, b):
    return np.linalg.solve(A, b)

# Пример использования
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
print(solve_linear_system(A, b))  # Output: [2. 3.]
