"""Мониторинг изменений в плейлистах

Задание: Разработать систему для отслеживания и анализа изменений в музыкальных плейлистах, 
используя название песен.

Подзадачи:
1. Предположим, что вы получаете ежедневные обновления плейлиста в виде списков названий песен.
2. Для каждого обновления плейлиста, используйте `deque` для хранения истории изменений последних 5 дней.
3. Используйте `Counter` для подсчета количества появлений каждой песни в этих 5 днях.
4. При каждом новом обновлении отображайте список песен, которые новые или исчезли из ротации. 
Вычислите, какие песни увеличивают и снижают свою популярность.

Усложнение: Сделайте анализ тенденций развития жанров в каждом плейлисте.
Для реализации задания, где требуется отслеживание изменений в плейлистах и анализ популярности песен, 
мы можем использовать Python с его стандартными библиотеками. """


from collections import deque, Counter

# Эмуляция прихода информации о плейлисте на 5 дней
playlist_data = [
    ["song1", "song2", "song3"],
    ["song1", "song2", "song4"],
    ["song1", "song2", "song5", "song3"],
    ["song2", "song6", "song7"],
    ["song1", "song2", "song8"]
]

# Создаем deque для хранения истории плейлистов (скользящее окно из последних 5 дней)
history_playlists = deque(maxlen=5)

# Counter для отслеживания количества появлений каждой песни в последние 5 дней
song_counter = Counter()

for daily_playlist in playlist_data:
    # Если history_playlists уже полон, удаляем информацию о самом старом плейлисте
    if len(history_playlists) == history_playlists.maxlen:
        oldest_playlist = history_playlists.popleft()
        for song in oldest_playlist:
            song_counter[song] -= 1
            if song_counter[song] == 0:
                del song_counter[song]
    
    # Добавляем новый плейлист и обновляем счетчики
    history_playlists.append(daily_playlist)
    song_counter.update(daily_playlist)
    
    # Выводим результаты
    print(f"Изменения на {len(history_playlists)} день:")
    print("\tТекущий плейлист: ", daily_playlist)
    print("\tЧастоты песен в последние 5 дней:", dict(song_counter))
    print("\tПесни во всех последних плейлистах:", {song for song, count in song_counter.items() if count == len(history_playlists)})
    print("\tНовые песни дня: ", set(daily_playlist) - set().union(*(history_playlists)))
    print("\tПесни, которые исчезли: ", set().union(*(history_playlists)) - set(daily_playlist))
