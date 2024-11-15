# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:00:24 2024

@author: 84982
"""
import itertools
def question_36(nums: list[int]) -> list[list[int]]:
    return [list(i) for i in itertools.permutations(nums)]
print(question_36([1,2,3]))
