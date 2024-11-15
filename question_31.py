# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 22:44:51 2024

@author: 84982
"""
import collections
def question_31(paragraph: str, n: int) -> list[str]:
    cac_tu = paragraph.split()
    dic_tu = dict(collections.Counter(cac_tu))
    so_tu = len(cac_tu)
    tu_nhieu = [tu for tu, so in dic_tu.items() if so / so_tu > 0.2 ]
    sap_xep_tu = sorted(tu_nhieu, key=lambda tu: dic_tu[tu], reverse= True)
    return sap_xep_tu[:n]
print(question_31("hello world hello universe hello", 1))
