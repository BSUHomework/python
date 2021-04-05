#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: primes.py.py
@time: 2021/3/20
@desc:
'''
def get_primes(n:int):
    num = []
    for i in range(2, n+1):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            num.append(i)
    return num

assert [2 , 3 , 5 , 7 , 11] == sorted ( get_primes ( 11 ) )