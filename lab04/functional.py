#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: functional.py.py
@time: 2021/3/26
@desc:
'''


class BoundedMeta(type):
    _count = {}
    @classmethod
    def __prepare__(cls, name, bases, *, max_instance_count=1):
        return super().__prepare__(name, bases)


    def __new__(cls, name, bases, ns, *, max_instance_count=1):
        cls._count[name] = 0
        return super(BoundedMeta,cls).__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, max_instance_count=1):
        self.max_instance_count = max_instance_count

        super().__init__(name, bases, ns)

    def __call__(cls, *args, **kwargs):
        cls._count[cls.__name__] += 1
        if not cls.max_instance_count:
            pass
        elif cls._count[cls.__name__] > cls.max_instance_count:
            raise TypeError
        return super().__call__(*args, **kwargs)

import abc
class BoundedBase(metaclass=BoundedMeta):
    @abc.abstractmethod
    def get_max_instance_count(cls):
        return 1

    def __new__(cls):

        cls.max_instance_count = cls.get_max_instance_count()
        return super().__new__(cls)


def smart_function(i=[0]):
    i[0]+=1
    return i[0]


if __name__ == '__main__':
    # class C(metaclass=BoundedMeta, max_instance_count=2):
    #     pass
    # c1 = C()
    # c2 = C()
    # try:
    #     c3 = C()
    # except TypeError:
    #     print('everything works fine !')
    # else:
    #     print('something goes wrong !')
    # class D(BoundedBase):
    #     @classmethod
    #     def get_max_instance_count(cls):
    #         return 1
    # d1 = D ()
    # try :
    #     d2 = D ()
    # except TypeError :
    #     print ('everything works fine !')
    # else :
    #     print ('something goes wrong !')
    for real_call_count in range(1, 5):
        assert smart_function() == real_call_count