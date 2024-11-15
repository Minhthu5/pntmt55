# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:14:11 2024

@author: 84982
"""
def question_23(nums: list[int]) -> bool:
    lis = []
    for i in nums:
        if i in lis:
            return True
        lis.append(i)
    return False
print(question_23([1,2,3,1]))

def question_23(nums: list[int]) -> bool:
    lis = []
    for i in nums:
        if i in lis:
            return True
        lis.append(i)
    return False
print(question_23([1, 2, 3, 4]))

