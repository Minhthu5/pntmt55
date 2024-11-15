# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:04:01 2024

@author: 84982
"""

def question_1(n: int) -> bool:
    if n<2:
       return False
    for i in range(2,n):
       if n % i == 0:
          return False
    return True
print(question_1(11))

def question_2(n: int)