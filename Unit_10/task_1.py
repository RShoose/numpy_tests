"""Операции над данными с использованием deque
Задание: Реализовать простой механизм скользящего окна для массива NumPy с использованием `collections.deque`.

Подзадачи:
1. Создайте массив NumPy.
2. Используйте `collections.deque` для создания скользящего окна заданной ширины и вычисление среднего значения для каждого окна.
3. Возвращайте список средних значений для каждого окна.
"""

from collections import deque
import numpy as np

def sliding_window_means(data):
    data = np.array(data)
    d = deque(maxlen=4)
    means = []
    for num in data:
        d.append(num)
        if len(d) == 4:
            means.append(np.mean(d))
    return means

# Пример использования
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [45, 78, 23, 56, 45, 34, 56, 98]
print(sliding_window_means(data))
