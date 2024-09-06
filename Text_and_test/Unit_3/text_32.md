# Мониторинг состояния сервера

## Задание:
Напишите функцию `server_monitor`, которая использует `deque` 
с ограниченной длиной для хранения последних статусов сервера (online/offline). 
Каждый новый статус добавляется в очередь, а при превышении лимита старые удаляются.
Функция должна анализировать состояния и выводить процент времени, когда сервер был онлайн.
## Пример вывода:
print(f"Server online {round(server_monitor(statuses))}% of the time.")


## Ответы:
### task_1:
Server online 80% of the time.

### task_2:
Server online 60% of the time.

### task_3:
Server online 43% of the time.
