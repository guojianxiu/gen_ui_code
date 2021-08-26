# coding: utf-8
# @Time : 2021/8/26 10:19 上午
# @Author : guojianxiu
# @File : gen_element_code.py
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


def gen_send_keys(name):
    return f"""
    def update_{name}(self, key):
        self.{name}.select_all()
        self.{name}.input(key)
        self.{name}.enter()
    """
