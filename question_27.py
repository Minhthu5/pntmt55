# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:53:03 2024

@author: 84982
"""

def question_27(strs: list[str]) -> str:
    tien_to = strs[0]
    for i in strs[1:]:
        while not i.startswith(tien_to):
            tien_to = tien_to[:-1]
            if not tien_to:
                return ""
    return tien_to
print(question_27(["minh", "min","miun"]))