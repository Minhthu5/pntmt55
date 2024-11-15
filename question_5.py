# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:21:36 2024

@author: 84982
"""

def question_5(lst: list, x: int) -> int or None:
    if x in lst:
        return lst.index(x)
    return None
print(question_5([1,2,3,4,5,6], 5))

