import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
import numpy as np
def random_normal(size, mean, std_dev):
    return np.random.normal(loc=mean, scale=std_dev, size=size)
    
result = random_normal(size, mean, std_dev)
    
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "srandom_normal"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            "size" : 4,
            'mean' : 0,
            'std_dev': 1
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

