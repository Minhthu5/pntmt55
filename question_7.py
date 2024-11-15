# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:56:36 2024

@author: 84982
"""
#Tạo danh sách n số thực ngẫu nhiên và tìm số lớn nhất,nhỏ nhất
import random
def question_7(n: int) -> (float, float):
    ds = []
    for i in range(n):
        x = random.uniform(0,1)
        ds.append(x)
    lon_nhat = max(ds)
    nho_nhat = min(x)
    return lon_nhat, nho_nhat
print(question_7(15))

