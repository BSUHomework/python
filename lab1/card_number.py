#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: card_number.py.py
@time: 2021/3/20
@desc:
'''


def check_card_number(card_number:int)->bool:
    digits = []
    while card_number != 0:
        digits = [card_number % 10] + digits
        card_number = card_number // 10

    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        d_0 = 2 * d
        d_1 = d_0 // 10
        d_2 = d_0 % 10
        checksum += d_1
        checksum += d_2

    return checksum % 10 == 0


def check_card_number_str(number:str)->bool:
    digits = [int(i) for i in number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        d_0 = 2 * d
        d_1 = d_0 // 10
        d_2 = d_0 % 10
        checksum += d_1
        checksum += d_2

    return checksum % 10 == 0


def generate_card_number(card:str)->str:
    import numpy as np
    while 1:
        result = list(np.random.randint(10, size=16))
        number = "".join([str(i) for i in result])
        if card == "visa":
            first_number = 4
            if check_card_number_str(number) and result[0] == first_number:
                return number
        elif card == "Mastercard":
            first_number = 5
            if check_card_number_str(number) and result[0] == first_number:
                return number
        else:
            if check_card_number_str(number):
                return number



assert check_card_number(5082337440657928)
assert not check_card_number_str('4601496706376197')
