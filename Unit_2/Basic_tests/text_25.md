# Использование `Counter` и `defaultdict`
Анализ логов веб-сервера

## Задание:
Разработайте функцию `analyze_web_logs`, которая анализирует список логов веб-сайта. Каждый лог представлен в виде кортежа, содержащего IP-адрес пользователя и URL, который он посетил. 
Функция должна возвращать словарь с количеством посещений каждого URL и словарь с количеством уникальных пользователей по каждому URL.

## Подзадачи:
1. Используйте `Counter` для подсчета посещений каждого URL.
2. Используйте `defaultdict` с множествами (`set`) для отслеживания уникальных IP-адресов, посещающих каждый URL.
3. После подсчета уникальных IP-адресов, преобразуйте множество в количество элементов для каждого URL.
4. Функция должна вернуть `url_visits`, `unique_ip_counts`

## Ответы:
### test_1:
Visits: Counter({'https://example.com/page1': 3, 'https://example.com/page2': 2, 'https://example.com/page3': 1})
Unique Visitors Per URL: {'https://example.com/page1': 2, 'https://example.com/page2': 2, 'https://example.com/page3': 1}


### test_2:
Visits: Counter({'https://example.com/home': 3, 'https://example.com/about': 2, 'https://example.com/contact': 1})
Unique Visitors Per URL: {'https://example.com/home': 3, 'https://example.com/about': 2, 'https://example.com/contact': 1}

### test_3:
Visits: Counter({'https://example.com/home': 4, 'https://example.com/about': 3, 'https://example.com/services': 2, 'https://example.com/contact': 1})
Unique Visitors Per URL: {'https://example.com/home': 3, 'https://example.com/about': 3, 'https://example.com/services': 2, 'https://example.com/contact': 1}