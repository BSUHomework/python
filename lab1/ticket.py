#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: ticket.py.py
@time: 2021/3/19
@desc:
'''
def get_nearest_lucky_ticket(number:int)->int:
        def loop1(number:int):
            numberlist = [i for i in str(number)]
            evensum = sum([int(i) for i in numberlist[::2]])
            oddsum = sum([int(i) for i in numberlist[1::2]])
            if  evensum==oddsum:return number
            else:               return loop1(number - 1)
        def loop2(number:int):
            numberlist = [i for i in str(number)]
            evensum = sum([int(i) for i in numberlist[::2]])
            oddsum = sum([int(i) for i in numberlist[1::2]])
            if  evensum==oddsum:return number
            else:               return loop2(number + 1)
        if abs(loop1(number) - number)> abs(loop2(number) - number):return loop2(number)
        else:return loop1(number)

assert get_nearest_lucky_ticket ( 111111 ) == 111111
assert get_nearest_lucky_ticket ( 123321 ) == 123321
assert get_nearest_lucky_ticket ( 123320 ) == 123321
assert get_nearest_lucky_ticket ( 333999 ) == 334004