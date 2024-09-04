"""Использование `Counter` и `defaultdict`
Анализ логов веб-сервера

Задание:
Разработайте функцию `analyze_web_logs`, которая анализирует список логов веб-сайта. Каждый лог представлен в виде кортежа, содержащего IP-адрес пользователя и URL, который он посетил. 
Функция должна возвращать словарь с количеством посещений каждого URL и словарь с количеством уникальных пользователей по каждому URL.

Подзадачи:
1. Используйте `Counter` для подсчета посещений каждого URL.
2. Используйте `defaultdict` с множествами (`set`) для отслеживания уникальных IP-адресов, посещающих каждый URL.
3. После подсчета уникальных IP-адресов, преобразуйте множество в количество элементов для каждого URL.
"""
from collections import Counter, defaultdict

def analyze_web_logs(logs):
    """
    Анализирует список логов веб-сайта, возвращая информацию о количестве посещений каждого URL,
    а также о количестве уникальных пользователей (IP-адресов) по каждому URL.
    
    :param logs: список кортежей (IP-адрес, URL)
    :return: tuple из двух словарей:
        1. Словарь с количеством посещений каждого URL.
        2. Словарь с количеством уникальных IP-адресов по каждому URL.
    """
    url_visits = Counter()        # Счетчик посещений URL
    unique_ips_per_url = defaultdict(set)  # defaultdict для отслеживания уникальных IP по URL
    
    # Проходим по каждому логу и агрегируем данные
    for ip, url in logs:
        # Учет посещений URL
        url_visits[url] += 1
        
        # Добавление IP в множество уникальных IP по данному URL
        unique_ips_per_url[url].add(ip)
    
    # Получаем количество уникальных IP-адресов по каждому URL
    unique_ip_counts = {url: len(ips) for url, ips in unique_ips_per_url.items()}
    
    return url_visits, unique_ip_counts

# Пример использования функции
"""logs = [
    ("192.168.1.1", "https://example.com/page1"),
    ("192.168.1.1", "https://example.com/page1"),
    ("192.168.1.2", "https://example.com/page1"),
    ("192.168.1.1", "https://example.com/page2"),
    ("192.168.1.3", "https://example.com/page2"),
    ("192.168.1.4", "https://example.com/page3"),
]"""
"""logs = [
    ("10.0.0.1", "https://example.com/home"),
    ("10.0.0.2", "https://example.com/about"),
    ("10.0.0.3", "https://example.com/home"),
    ("10.0.0.1", "https://example.com/contact"),
    ("10.0.0.4", "https://example.com/about"),
    ("10.0.0.5", "https://example.com/home"),
]"""

logs = [
    ("172.16.0.1", "https://example.com/home"),
    ("172.16.0.2", "https://example.com/about"),
    ("172.16.0.1", "https://example.com/home"),
    ("172.16.0.3", "https://example.com/services"),
    ("172.16.0.4", "https://example.com/home"),
    ("172.16.0.2", "https://example.com/contact"),
    ("172.16.0.5", "https://example.com/services"),
    ("172.16.0.1", "https://example.com/about"),
    ("172.16.0.3", "https://example.com/home"),
    ("172.16.0.6", "https://example.com/about"),
]


visits, unique_visitors = analyze_web_logs(logs)
print("Visits:", visits)
print("Unique Visitors Per URL:", unique_visitors)

# Вывод:
# Visits: Counter({'https://example.com/page1': 3, 'https://example.com/page2': 2, 'https://example.com/page3': 1})
# Unique Visitors Per URL: {'https://example.com/page1': 2, 'https://example.com/page2': 2, 'https://example.com/page3': 1}