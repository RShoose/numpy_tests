import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import OrderedDict

def user_registration(users):
    registry = OrderedDict()
    for name, age in users:
        registry[name] = age
    return list(registry.items())
    
result = user_registration(users)    
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "user_registration"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "users" : [("Alice", 25), ("Bob", 30), ("Charlie", 28)]
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

    
    