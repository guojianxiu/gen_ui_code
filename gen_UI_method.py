# coding: utf-8
# @Time : 2021/8/25 5:34 下午
# @Author : guojianxiu
# @File : gen_UI_method.py
import os
import re

from gen_element_code import *


def get_files(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            code = ''
            length = 0
            if os.path.splitext(file)[1] == '.py':
                print(os.path.join(root, file))
                with open(os.path.join(root, file), 'r') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if re.search('=', line) and re.search('NewPageElement', line):
                            ele_name = line.split('=')[0].strip()
                            print(ele_name)
                            a = gen_get_text(ele_name)
                            b = gen_get_class(ele_name)
                            c = gen_click(ele_name)
                            d = ''
                            if re.search('input', line):
                                d = gen_send_keys(ele_name)
                            code = code + a + b + c + d
                        if re.search('self.is_finish_AI()', line):
                            length = i
                lines = lines[0:length+1]
                lines.append(code)
                with open(os.path.join(root, file), 'r+') as f:
                    f.write(''.join(lines))


if __name__ == '__main__':
    # 本地文件路径，想要生成code的的所在文件夹
    file_path = '/Users/gjx/PycharmProjects/work_scripts/test_file'
    get_files(file_path)
