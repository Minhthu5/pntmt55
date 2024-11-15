# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:58:12 2024

@author: 84982
"""
def question_25(nums: list[int]) -> list[int]:
    nums_new = sorted([i**2 for i in nums])
    return nums_new
print(question_25([-4, -1, 0, 3, 10]))





