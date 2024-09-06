import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import deque, Counter

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
    
    
print(f"Изменения на {len(history_playlists)} день:")
    print("Текущий плейлист: ", daily_playlist)
    print("Частоты песен в последние 5 дней:", dict(song_counter))
    print("Песни во всех последних плейлистах:", {song for song, count in song_counter.items() if count == len(history_playlists)})
    print("Новые песни дня: ", set(daily_playlist) - set().union(*(history_playlists)))
    print("Песни, которые исчезли: ", set().union(*(history_playlists)) - set(daily_playlist))
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = ""
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = '''playlist_data = [
                        ["song1", "song2", "song3"],
                        ["song1", "song2", "song4"],
                        ["song1", "song2", "song5", "song3"],
                        ["song2", "song6", "song7"],
                        ["song1", "song2", "song8"]
                        ]'''
        add_after = ""

        arguments = {}

        fake_arguments = {}

        self.default_test(
            class_name=class_name,
            class_args=class_args,
            method_name=method_name,
            attr_name=attr_name,
            need_to_eval=need_to_eval,
            arguments=arguments,
            fake_arguments=fake_arguments,
            correct_code=CORRECT_CODE,
            correct_code_language=CORRECT_CODE_LANGUAGE,
            var_name=var_name,
            formulation=formulation,
            need_print=need_print,
            add_before=add_before,
            add_after=add_after,
        )

