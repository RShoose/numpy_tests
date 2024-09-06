"""Интеграция NumPy и deque для обработки временных рядов
Задание: Сгладить временной ряд, используя метод простого экспоненциального сглаживания с помощью `deque`.

Подзадачи:
1. Создайте массив NumPy, представляющий временной ряд.
2. Используйте `collections.deque` для хранения недавних значений и реализуйте простое экспоненциальное сглаживание.
3. Верните сглаженный временной ряд.
"""

from collections import deque
import numpy as np
np.random.seed(21)

def exponential_smoothing(data, alpha=0.1):
    smoothed_data = []
    d = deque([data[0]], maxlen=2)  # начнем с первого элемента
    for value in data[1:]:
        new_smooth = alpha * value + (1 - alpha) * d[0]
        smoothed_data.append(new_smooth)
        d.appendleft(new_smooth)
    return np.array(smoothed_data)  # Возвращаем NumPy массив для удобства

# Пример использования
time_series = np.random.rand(10)
print(time_series)
smoothed_series = exponential_smoothing(time_series)
print(smoothed_series)