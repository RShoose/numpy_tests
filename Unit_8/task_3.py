"""Нормализация вектора
Задание: Создать функцию для нормализации вектора (приведения его к единичной длине)."""

import numpy as np
def normalize_vector(v):
    norm = np.linalg.norm(v)
    return v / norm if norm != 0 else np.zeros_like(v)

# Пример использования
v1 = np.array([1, 2, 3])
print(normalize_vector(v1))  # Output: [0.26726124 0.53452248 0.80178373]
