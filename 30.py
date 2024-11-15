# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:07:15 2024

@author: 84982
"""
def question_30(paragraph: str) -> dict[str, int]:
    dic = {}
    cac_tu = paragraph.split()
    for tu in cac_tu:
        if tu in dic:
            dic[tu] += 1
        else:
            dic[tu] = 1
    return dic

import collections
def question_30_c2(paragraph: str) -> dict[str, int]:
    cac_tu = paragraph.split()
    dic_tu = dict(collections.Counter(cac_tu))
    return dic_tu
print(question_30("apple orange apple banana orange"))
print(question_30("hello world hello"))