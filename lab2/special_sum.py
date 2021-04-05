#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: special_sum.py.py
@time: 2021/3/20
@desc:
'''
def calculate_special_sum(n:int):
    sumdata = 0
    while n>=1:
        sumdata += ((n - 1) ** 2) * n
        n=n-1
    return sumdata

assert calculate_special_sum ( 3 ) == 14