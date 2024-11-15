# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:33:08 2024

@author: 84982
"""
from typing import Optional
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    lis = [] 
    for i in nums:
        so_t2 = target - i
        if so_t2 in lis:    
            return (so_t2, i)
        lis.append(i)
    return None
if __name__=="__main__":
    print(question_21([2, 7, 11, 15], 9))
    

