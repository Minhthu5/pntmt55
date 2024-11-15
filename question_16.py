# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:18:06 2024

@author: 84982
"""
#Tính trung bình cộng của nhiều tham số
def question_16(*args) -> float:
    if not args:
        return None
    return sum(args) / len(args)
print(question_16(1, 2, 3, 4, 5))

