#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: unique.py.py
@time: 2021/3/20
@desc:
'''

def compress(arg:list)->list:
    n=len(arg)
    data = {}
    while n>0:
        if str(arg[n-1])in data.keys() :
            data[str(arg[n - 1])]=data[str(arg[n-1])]+1
        else:
            data[str(arg[n-1])]=1
        n=n-1
    return [(int(key),value)for key,value in data.items()]



expected_sorted = [(1, 2), (2, 1), (3, 1)]
actual_sorted = sorted(compress([1, 2, 1, 3]))
assert expected_sorted == actual_sorted