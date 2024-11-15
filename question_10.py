# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:49:54 2024

@author: 84982
"""
#Nhập danh sách số nguyên và kiểm tra danh sách trống
def question_10()-> None:
    n = input("Nhap so nguyen (phan cach bang khoang trang): ")
    ds = [int(i) for i in n.split()]
    if not ds:
        return None
    return ds
print(question_10())

