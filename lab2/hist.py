#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: hist.py.py
@time: 2021/3/20
@desc:
'''

def distribute(sample:list,k:int)->list:
    maximum = max(sample)
    minimum = min(sample)
    h= float(maximum) - float(minimum)
    cell_length = float(h)/k
    dicts = {str(i+1):0 for i in range(0,k)}
    for i in sample:
        if i == minimum:
            dicts["1"] = dicts["1"]+1
        elif i == maximum:
            dicts[str(k)] = dicts[str(k)] + 1
        else:
            key = int((i-minimum)/cell_length)+1
            dicts[str(key)] = dicts[str(key)]+1
    return list(dicts.values())



assert distribute([1.25 , 1 , 2 , 1.75], 2 ) == [2 , 2]