import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import defaultdict
import re

def index_documents(documents):
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
    
    
result = index_documents(documents)
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "index_documents"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "documents" : ["Hello world, welcome to the universe.",
                           "Hello again! The world is beautiful.",
                           "The universe is vast and full of stars."]
            }

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

    def test_2(self):
        class_name = ""
        class_args = ""
        method_name = "index_documents"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "documents" : [
                "Время летит, и каждый момент уникален.",
                "Снова встречаемся! Жизнь полна удивительных событий.",
                "Мир вокруг нас красив и полон загадок.",
                "Каждый день — это новая возможность для открытий.",
                "Светит солнце, и природа пробуждается к жизни."]
            }

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

    def test_3(self):
        class_name = ""
        class_args = ""
        method_name = "index_documents"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "documents" : ["Привет, мир! Welcome to the universe.",
                    "Снова привет! The world is beautiful.",
                    "Вселенная огромна и full of stars.",
                    "Каждый день — это a new opportunity.",
                    "Светит солнце, and nature awakens to life."]
            }

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
