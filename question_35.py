# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:58:39 2024

@author: 84982
"""
def question_35(s: str) -> str:
    n = len(s)
    chuoi_dai = ""
    for i in range(n):
        for j in range(i+1, n):
            chuoi = s[i:j]
            if s.count(chuoi) > 1:
                if len(chuoi) > len(chuoi_dai):
                    chuoi_dai = chuoi
    return chuoi_dai
print(question_35("aabcdeaabcd"))