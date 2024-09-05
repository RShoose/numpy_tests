"""Обслуживание клиентов

Задание:
Напишите функцию `process_clients`, которая использует `deque` для обработки списка клиентов, где кажому клиенту выдают номерок.
Клиенты с четными номерами обслуживаются первыми (с начала очереди), с нечетными — последними (с конца очереди). 
Функция должна возвращать список имен клиентов в порядке обслуживания.
"""


from collections import deque

def process_clients(clients):
    queue = deque()
    for index, client in enumerate(clients, 1):
        if index % 2 == 0:
            # Индекс четный, добавляем в начало очереди
            queue.appendleft(client)
        else:
            # Индекс нечетный, добавляем в конец очереди
            queue.append(client)
    return list(queue)

clients = ["Alice", "Bob", "Charlie", "David"]
# clients = ["Андрей", "Степан", "Олег", "Владимир", "Олег"]
print(process_clients(clients))  # Верный вывод: ['Charlie', 'Alice', 'Bob', 'David']