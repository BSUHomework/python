#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: utils.py.py
@time: 2021/3/23
@desc:
'''
from functools import wraps
import timeit

def profile(func):
    @wraps(func)
    def running(*args, **kwargs):
        starttime = timeit.default_timer()
        result = func()
        print("running time is :", timeit.default_timer() - starttime)
        print(f"the result is :{result}")
        return func(*args, **kwargs)

    return running




class timer():
        def __enter__(self):
            self.starttime = timeit.default_timer()
            print("the start time is :", self.starttime)
        def __exit__(self, type, value, trace):
            print("running time is :", timeit.default_timer() - self.starttime)\


if __name__ == '__main__':


    @profile
    def some_function ():
        return sum( range ( 1000 ) )
    result = some_function () #

    with timer ():
        print ( sum ( range ( 1000 ) ) )