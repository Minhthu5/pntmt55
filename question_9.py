# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:18:31 2024

@author: 84982
"""
#Kiểm tra chuỗi palindrome
def question_9(s: str) -> bool:
    chuoi_s = ''.join(i.lower() for i in s if i.isalnum())
    chuoi_s_dao = chuoi_s[::-1]
    return chuoi_s == chuoi_s_dao
print(question_9("A man, a plan, a canal: Panama"))

