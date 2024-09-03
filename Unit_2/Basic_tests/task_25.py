import os
import sys

dirname = os.path.dirname(__file__)
module_path = os.path.join(dirname, "..")
sys.path.append(module_path)

from AbstractTest2 import AbstractTest2, RunCode, process, wrapper

CORRECT_CODE = r"""
from collections import Counter, defaultdict

def analyze_web_logs(logs):
    url_visits = Counter()        # Счетчик посещений URL
    unique_ips_per_url = defaultdict(set)  # defaultdict для отслеживания уникальных IP по URL
    
    # Проходим по каждому логу и агрегируем данные
    for ip, url in logs:
        # Учет посещений URL
        url_visits[url] += 1
        
        # Добавление IP в множество уникальных IP по данному URL
        unique_ips_per_url[url].add(ip)
    
    # Получаем количество уникальных IP-адресов по каждому URL
    unique_ip_counts = {url: len(ips) for url, ips in unique_ips_per_url.items()}
    
    return url_visits, unique_ip_counts
    
    
visits, unique_visitors = analyze_web_logs(logs)
print("Visits:", visits)
print("Unique Visitors Per URL:", unique_visitors)
"""

CORRECT_CODE_LANGUAGE = "Python"


class Tests(AbstractTest2):
    def test_1(self):
        class_name = ""
        class_args = ""
        method_name = "analyze_web_logs"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = ""

        arguments = {
            "logs" : [
                    ("192.168.1.1", "https://example.com/page1"),
                    ("192.168.1.1", "https://example.com/page1"),
                    ("192.168.1.2", "https://example.com/page1"),
                    ("192.168.1.1", "https://example.com/page2"),
                    ("192.168.1.3", "https://example.com/page2"),
                    ("192.168.1.4", "https://example.com/page3"),
                    ]
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
        method_name = "analyze_web_logs"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = ""

        arguments = {
            "logs" : [
                    ("10.0.0.1", "https://example.com/home"),
                    ("10.0.0.2", "https://example.com/about"),
                    ("10.0.0.3", "https://example.com/home"),
                    ("10.0.0.1", "https://example.com/contact"),
                    ("10.0.0.4", "https://example.com/about"),
                    ("10.0.0.5", "https://example.com/home"),
                    ]
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
        method_name = "analyze_web_logs"
        var_name = ""
        attr_name = ""
        need_to_eval = False
        formulation = ""
        need_print = False
        add_before = ""
        add_after = ""

        arguments = {
            "logs" : [
                        ("172.16.0.1", "https://example.com/home"),
                        ("172.16.0.2", "https://example.com/about"),
                        ("172.16.0.1", "https://example.com/home"),
                        ("172.16.0.3", "https://example.com/services"),
                        ("172.16.0.4", "https://example.com/home"),
                        ("172.16.0.2", "https://example.com/contact"),
                        ("172.16.0.5", "https://example.com/services"),
                        ("172.16.0.1", "https://example.com/about"),
                        ("172.16.0.3", "https://example.com/home"),
                        ("172.16.0.6", "https://example.com/about"),
                    ]
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