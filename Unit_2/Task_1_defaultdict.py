"""Индексирование документов по словам

Задание:
Создайте функцию `index_documents`, которая принимает список строк (где каждая строка представляет документ) и возвращает `defaultdict`, где каждый ключ - это слово, а значение - список индексов документов, в которых это слово встречается.

Подзадачи:
1. Инициализируйте `defaultdict` с типом `set` для избежания дубликатов.
2. Пройдите по всем документам, для каждого слова в документе добавьте индекс документа в соответствующее множество.
3. В конце преобразуйте все значения из `set` в `list`.
"""
from collections import defaultdict
import re

def index_documents(documents):
    """
    Принимает список строк, где каждая строка - это документ. Возвращает `defaultdict`,
    в котором ключи - это слова, а значения - списки индексов документов, содержащих эти слова.
    
    :param documents: список документов (list of str)
    :return: defaultdict с множествами индексов документа для каждого слова
    """
    # Создаем defaultdict с типом set для автоматического создания множеств при новом ключе
    word_index = defaultdict(set)
    
    # Итерация по документам с сохранением индекса
    for index, doc in enumerate(documents):
        # Очистка и разбиение документа на слова, игнорируя пунктуацию
        words = re.findall(r'\b\w+\b', doc.lower())
        # Добавление индекса документа в множество для каждого слова
        for word in words:
            word_index[word].add(index)
    
    # Преобразование множеств в списки для удобства использования
    for word in word_index:
        word_index[word] = list(word_index[word])
    
    return word_index

# Пример использования функции
documents = [
    "Hello world, welcome to the universe.",
    "Hello again! The world is beautiful.",
    "The universe is vast and full of stars."
]

result = index_documents(documents)
print(result)
# Ожидаемый вывод (пример): defaultdict(<class 'set'>, {'hello': [0, 1], 'world': [0, 1], 'welcome': [0], 'to': [0], 'the': [1, 2], ...})