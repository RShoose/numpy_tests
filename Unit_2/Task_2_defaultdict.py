"""Тема: Составление статистики по возрастам

Задание:
Создайте функцию `age_statistics`, которая принимает список возрастов людей и классифицирует их по группам: "children" (0-14 лет), "youth" (15-24 лет), "adults" (25-64 лет), "seniors" (65 лет и старше), используя `defaultdict`.

Подзадачи:
1. Инициализируйте `defaultdict` с типом `list`.
2. Пройдите через список возрастов, добавив каждый возраст в соответствующую категорию.
"""
from collections import defaultdict

def age_statistics(ages):
    """
    Классифицирует список возрастов людей по возрастным категориям с использованием defaultdict.
    
    :param ages: список возрастов (list of int)
    :return: словарь с возрастными группами как ключами и списками возрастов как значениями
    """
    # Создаем defaultdict с типом list для автоматического создания списка при новом ключе
    age_groups = defaultdict(list)
    
    # Определяем возрастные группы и добавляем возрасты в соответствующие категории
    for age in ages:
        if age <= 14:
            age_groups['children'].append(age)
        elif 15 <= age <= 24:
            age_groups['youth'].append(age)
        elif 25 <= age <= 64:
            age_groups['adults'].append(age)
        else:  # 65 и старше
            age_groups['seniors'].append(age)
    
    return age_groups

# Пример использования функции
age_list = [10, 20, 25, 30, 65, 70, 14, 22, 23, 64, 45]
result = age_statistics(age_list)
print(result)
# Ожидаемый вывод: defaultdict(<class 'list'>, {'children': [10, 14], 'youth': [20, 22, 23], 'adults': [25, 30, 64, 45], 'seniors': [65, 70]})