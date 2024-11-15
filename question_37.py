# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 23:13:38 2024

@author: 84982
"""
def question_37(s: str) -> bool:
    dic_ky_tu = {')':'(', '}':'{', ']':'['}
    ds_ngoac_mo = []
    for i in s:
        if i in dic_ky_tu.values():
            ds_ngoac_mo.append(i)
        elif i in dic_ky_tu:
            if ds_ngoac_mo and ds_ngoac_mo[-1] == dic_ky_tu[i]:
                ds_ngoac_mo.pop()
            else:
                return False
    return True if not ds_ngoac_mo else False
print(question_37("()"))
print(question_37("()[]{}"))
print(question_37("(]"))
print(question_37("([)]"))
print(question_37("{[]}"))