"""Фильтрация элементов в трехмерном массиве
Задание: Построить функцию, которая принимает трехмерный массив 
и возвращает двумерный массив, который содержит
только те элементы каждого подмассива второго уровня,
которые больше среднего значения всех элементов в соответствующем подмассиве."""

import numpy as np

def filter_elements_3d(arr):
    result = []
    for matrix in arr:
        local_result = []
        for subarray in matrix:
            mean_value = sum(subarray) / len(subarray)  # Вычисляем среднее значение
            # Формируем список элементов больше или равных среднему
            filtered_elements = [x for x in subarray if x >= mean_value]
            local_result.append(filtered_elements)
        result.append(local_result)
    return result

# Пример входных данных и вызов функции
example_3d_array = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9, 10], [10, 11, 12, 13]]]
example_3d_array = [[[7, 9, 6], [10, 11, 12]], [[2, 8, 6], [10, 15]]]
print(filter_elements_3d(example_3d_array))