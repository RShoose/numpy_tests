import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import deque
import numpy as np

def exponential_smoothing(data):
    data = np.array(data)
    smoothed_data = []
    alpha=0.1
    d = deque([data[0]], maxlen=2)  # начнем с первого элемента
    for value in data[1:]:
        new_smooth = alpha * value + (1 - alpha) * d[0]
        smoothed_data.append(new_smooth)
        d.appendleft(new_smooth)
    return np.array(smoothed_data)
    
result = exponential_smoothing(data)  
    
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "exponential_smoothing"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {"data" : [0.04872488, 0.28910966, 0.72096635,
                               0.02161625, 0.20592277, 0.05077326,
                               0.30227189, 0.66391029, 0.30811439, 0.58359128]}

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

 