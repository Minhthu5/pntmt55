# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:48:50 2024

@author: 84982
"""
#Tính số Fibonacci thứ n
def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b
print(question_11(5))
