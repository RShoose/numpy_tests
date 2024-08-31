"""Мониторинг состояния сервера

Задание:
Напишите функцию `server_monitor`, которая использует `deque` 
с ограниченной длиной для хранения последних статусов сервера (online/offline). 
Каждый новый статус добавляется в очередь, а при превышении лимита старые удаляются.
Функция должна анализировать состояния и выводить процент времени, когда сервер был онлайн."""



from collections import deque

def server_monitor(statuses, capacity=10):
    dq = deque(maxlen=capacity)
    dq.extend(statuses)
    online_count = sum(1 for status in dq if status == 'online')
    return (online_count / len(dq)) * 100

statuses = ["online", "online", "offline", "online", "online", "offline", "online", "online", "online", "online"]
print(f"Server online {server_monitor(statuses)}% of the time.")
