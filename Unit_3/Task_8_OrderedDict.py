"""Тема: Регистрация информации о пользователях

Задание:
Создайте функцию `user_registration`, использующую `OrderedDict` 
для сохранения пользовательских данных 
(имя и возраст) в порядке ввода и возвращающую этот порядок 
при запросе списка пользователей."""


from collections import OrderedDict

def user_registration(users):
    registry = OrderedDict()
    for name, age in users:
        registry[name] = age
    return list(registry.items())

users = [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
print(user_registration(users))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 28)]
