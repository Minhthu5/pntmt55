# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:04:44 2024

@author: 84982
"""
def question_29(nums: list[int]) -> float:
    nums.sort()
    so_pt = len(nums)
    if so_pt % 2 != 0:
        return nums[(so_pt - 1) // 2]
    else:
        so_giua_1 = nums[(so_pt // 2) -1]
        so_giua_2 = nums[so_pt // 2]
        so_trung_vi = (so_giua_1 + so_giua_2) / 2
        return so_trung_vi
print(question_29(([1, 2, 3, 4])))
