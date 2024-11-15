# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:55:30 2024

@author: 84982
"""
def question_34(s: str) -> int:
    danh_sach = []
    do_dai_max = 0
    for i in s:
        while i in danh_sach:
            danh_sach.pop(0)
        danh_sach.append(i)
        do_dai_max = max(do_dai_max, len(danh_sach))
    return do_dai_max
print(question_34("abcabcbb"))