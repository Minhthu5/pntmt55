# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:53:02 2024

@author: 84982
"""

def question_33(nums: list[int]) -> tuple[int, int]:
    if len(nums) >= 5:
        giam_dan = sorted(nums, reverse= True)
        pt_lon_2 = giam_dan[1]
        tang_dan = sorted(nums)
        pt_nho_5 = tang_dan[4]
        return (pt_lon_2, pt_nho_5)
    else:
        return None
print(question_33([3, 1, 4, 5, 9, 2, 6, 8, 7]))
