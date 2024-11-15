# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 09:31:51 2024

@author: 84982
"""
def question_24(nums: list[int]) -> int:
    phan_tu = None
    dem = 0
    for i in nums:
        if dem == 0:
            phan_tu = i
        dem += (1 if i == phan_tu else -1)
    return phan_tu

def question_24_c2(nums: list[int]) -> int:
    n = len(nums)
    nums.sort()
    return nums[n//2]

import collections
def question_24_c3(nums: list[int]) -> int:
    n = len(nums)
    dic_phantu_soluong = collections.Counter(nums)
    for phantu, soluong in dic_phantu_soluong.items():
        if soluong > n//2:
            return phantu
if __name__=="__main__":
    print(question_24([3,2,3]))
    print(question_24([3,2,3]))
    print(question_24([3,2,3]))


