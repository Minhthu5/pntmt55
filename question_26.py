# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:34:03 2024

@author: 84982
"""

def question_26(s: str) -> int:
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    do_dai = 0
    ky_tu_giua = False
    for i in dic.values():
        if i % 2 == 0:
            do_dai += i
        else:
            do_dai += i - 1
            ky_tu_giua = True
    if ky_tu_giua:
        do_dai += 1
    return do_dai

import collections
def question_26_c2(s: str) -> int:
    dic_tu_so = collections.Counter(s)
    do_dai = 0
    co_so_le = False
    for so in dic_tu_so.values():
        do_dai += so // 2 * 2    
        if so % 2 == 1:
            co_so_le = True
    if co_so_le:
        do_dai += 1
    return do_dai
print(question_26("abccccdd"))
print(question_26_c2("aaaaa"))

