# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:31:54 2024

@author: 84982
"""
import random
def question_17(n: int) -> list:
    danh_sach = []
    for i in range(n):
        x =random.randint(1, 100)
        danh_sach.append(x)
    danh_sach.sort(reverse= True)
    return danh_sach
print(question_17(5))
    
# tạo và sắp xếp danh sách số nguyên ngaux nhiên theo thứ tự giảm dần
import random
def question_17(n: int) -> list:
    ds = []
    for i in range(n):
        x = random.randint(1,100)
        ds.append(x)
    ds.sort(reverse= True)
    return ds

    
    