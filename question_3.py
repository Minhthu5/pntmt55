# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:57:47 2024

@author: 84982
"""
def question_3(s: str) -> (int, int):
    so_ki_tu_hoa = 0
    so_ki_tu_thuong = 0
    for ki_tu in s:
        if ki_tu.isupper():
            so_ki_tu_hoa += 1
        elif ki_tu.islower():
            so_ki_tu_thuong += 1
    return so_ki_tu_hoa, so_ki_tu_thuong
print(question_3("hello Minh Thu"))