# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:03:36 2024

@author: 84982
"""
import collections
def question_28(s: str) -> dict[str, int]:
    dic_ky_tu = dict(collections.Counter(s))
    return dic_ky_tu
print(question_28("hello"))