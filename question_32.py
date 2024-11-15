# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:50:47 2024

@author: 84982
"""
def  question_32(nums: list[int]) -> tuple[list[int], list[int]]:
    ds_chan_giam = sorted([i for i in nums if i % 2 == 0], reverse= True)
    ds_le_tang = sorted([ i for i in nums if i % 2 != 0])
    Tuple = (ds_chan_giam, ds_le_tang)
    return Tuple
print(question_32([4, 1, 3, 2, 7, 8, 5]))
