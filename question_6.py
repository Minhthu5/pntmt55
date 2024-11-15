# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:30:11 2024

@author: 84982
"""

def question_6(n: int):
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua *= i
    return giai_thua
print(question_6(4))
                   
