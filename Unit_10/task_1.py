"""Операции над данными с использованием deque
Задание: Реализовать простой механизм скользящего окна для массива NumPy с использованием `collections.deque`.

Подзадачи:
1. Создайте массив NumPy.
2. Используйте `collections.deque` для создания скользящего окна заданной ширины и вычисление среднего значения для каждого окна.
3. Возвращайте список средних значений для каждого окна.
"""

from collections import deque
import numpy as np

def sliding_window_means(data, window_size=3):
    d = deque(maxlen=window_size)
    means = []
    for num in data:
        d.append(num)
        if len(d) == window_size:
            means.append(np.mean(d))
    return means

# Пример использования
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sliding_window_means(data, 4))
