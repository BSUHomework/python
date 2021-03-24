#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: merge.py
@time: 2021/3/20
@desc:
'''
def merge(args1:tuple or list,args2:tuple or list)->tuple or list:
    _arg1=list(args1)
    _arg2=list(args2)
    result = []

    while len(_arg1) > 0 and len(_arg2) > 0:
        if _arg1[0] < _arg2[0]:
            result.append(_arg1[0])
            del _arg1[0]
        else:
            result.append(_arg2[0])
            del _arg2[0]
    result.extend(_arg1)
    result.extend(_arg2)
    if type(args1) == type([]):
        return result
    else:
        return tuple(result)

assert merge ([1 , 2 , 7], [3]) == [1 , 2 , 3 , 7]
assert merge (( 3 , 15 ) , (7 , 8 ) ) == (3 , 7 , 8 , 15 )
