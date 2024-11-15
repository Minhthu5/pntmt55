# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:19:38 2024

@author: 84982
"""
def question_1(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(question_1(11))

        
