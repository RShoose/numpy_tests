# Анализ частоты слов в тексте

## Задание:
Напишите функцию `calculate_word_frequency`, которая получает строку текста и возвращает словарь, где ключами являются слова, а значениями - частоты этих слов в тексте. Используйте `Counter` из модуля `collections`.

## Подзадачи:
1. Преобразуйте весь текст к нижнему регистру для унификации.
2. Разбейте текст на слова, учитывая только алфавитные символы (уберите пунктуацию).
3. Используйте `Counter` для подсчёта количества каждого слова.

## Ответы:
### task_1:
Counter({'hello': 2, 'world': 1})

### task_2:
Counter({'учится': 3, 'и': 1, 'еще': 1, 'раз': 1})

### task_3:
Counter({'the': 2, 'at': 2, 'кот': 1, 'cat': 1, 'сидит': 1, 'sits': 1, 'на': 1, 'on': 1, 'окне': 1, 'window': 1, 'смотрит': 1, 'looks': 1, 'птиц': 1, 'birds': 1})
