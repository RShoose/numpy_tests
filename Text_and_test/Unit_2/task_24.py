import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import defaultdict

def age_statistics(ages):
    # Определяем возрастные группы и добавляем возрасты в соответствующие категории
    for age in ages:
        if age <= 14:
            age_groups['children'].append(age)
        elif 15 <= age <= 24:
            age_groups['youth'].append(age)
        elif 25 <= age <= 64:
            age_groups['adults'].append(age)
        else:  # 65 и старше
            age_groups['seniors'].append(age)
    
    return age_groups

# Пример использования функции

result = age_statistics(age_list)

"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "age_statistics"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "age_list" : [10, 20, 25, 30, 65, 70, 14, 22, 23, 64, 45]
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
        method_name = "age_statistics"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "age_list" : [-10, 38, 75, 30, 65, 180, 23, 0, 45]
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
        method_name = "age_statistics"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "age_list" : [23, 45, 67, 12, 34, 89, 56, 78, 90, 5]
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