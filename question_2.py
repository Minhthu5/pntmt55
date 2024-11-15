# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:34:09 2024

@author: 84982
"""
import random
def question_2(n):
    ds = []
    for i in range(n):
     number =random.randint(1,100)
     ds.append(number)
     tong = sum(ds)
     trungbinh = tong / n
    return tong, trungbinh
print(question_2(5))

