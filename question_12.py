# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:54:42 2024

@author: 84982
"""
#Tạo số nguyên ngẫu nhiên và kiểm tra số nguyên tố
import random
def question_12() -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
n = random.randint(1,1000)
print(f"So ngau nhien: {n}")
print(question_12())

