"""Свойства массива
Задание: Создайте любой массив и выведите его форму (размерности),
размер (общее количество элементов) и тип данных элементов массива."""

import numpy as np
# Создание массива
array_2 = np.array([[2, 4, 6], [8, 10, 12]], dtype=np.int32)

print("Форма массива:", array_2.shape)
print("Размер массива:", array_2.size)
print("Тип данных массива:", array_2.dtype)
