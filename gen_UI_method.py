# coding: utf-8
# @Time : 2021/8/25 5:34 下午
# @Author : guojianxiu
# @File : gen_UI_method.py
import os
import re


def get_files(file_dir):
    code = ''
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.py':
                print(os.path.join(root, file))
                with open(os.path.join(root, file), 'r') as f:
                    for i, line in enumerate(f.readlines()):
                        if re.search('=', line) and re.search('NewPageElement', line):
                            ele_name = line.split('=')[0].strip()
                            print(ele_name)
                            a = gen_get_text(ele_name)
                            b = gen_get_class(ele_name)
                            c = gen_click(ele_name)
                            code = code + a + b + c
                        if re.search('=', line) and re.search('PageElements', line):
                            ele_name = line.split('=')[0].strip()
                            print(ele_name)
                            a = gen_get_text(ele_name)
                            b = gen_get_class(ele_name)
                            c = gen_click(ele_name)
                            code = code + a + b + c
                    print(code)
                with open(os.path.join(root, file), 'a+') as f:
                    f.write(code)


def gen_get_text(name):
    return f"""
    def get_{name}_text(self):
        return self.{name}.text
            """


def gen_get_class(name):
    return f"""
    def get_{name}_status(self):
        if 'status' in self.{name}.get_attribute('class'):
            return True
        return False
        """


def gen_click(name):
    return f"""
    def click_{name}(self):
        self.{name}.click()
    """


if __name__ == '__main__':
    file_path = '/Users/gjx/PycharmProjects/work_scripts/test_file'
    get_files(file_path)
