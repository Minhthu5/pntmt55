# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:20:02 2024

@author: 84982
"""
def question_39(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    gia_max = 0
    mua_min = prices[0]
    for i in prices[1:]:
        gia_max = max(gia_max, i - mua_min)
        mua_min = min(mua_min, i)
    return gia_max
print(question_39([6, 7, 8, 9, 20, 5]))
