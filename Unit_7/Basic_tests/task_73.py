import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
import numpy as np
def transpose_matrix(matrix):
    matrix = np.array(matrix)
    return matrix.T
    
    
result = transpose_matrix(matrix)
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "transpose_matrix"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            'matrix' : [[1, 2, 3], [4, 5, 6]]
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
        method_name = "transpose_matrix"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
            'matrix' : [[[4, 5, 6], [9, 8, 7]], [[6, 4, 5], [4, 7, 9]], [[1, 5, 4], [7, 5, 6]]]
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
        method_name = "transpose_matrix"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = True
        add_before = ""
        add_after = ""

        arguments = {
           'matrix' : [[1, 2], [3, 4], [5, 6]]
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
