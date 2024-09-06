"""Перетасовка элементов массива
Задание: Написать функцию для случайной перетасовки элементов массива."""

import numpy as np
def shuffle_array(array):
    array = np.array(array)
    np.random.shuffle(array)
    return array

# Пример использования
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(shuffle_array(arr))
