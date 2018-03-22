#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex29.py
잘못된 입력 처리
"""


import math


if __name__ == '__main__':
    years = 0

    while True:
        try:
            r = int(input('What is the rate of return? '))
            years = math.ceil(72/r)
            print('It will take {} years to double your initial investment. '.format(years))
            break
        except ZeroDivisionError:
            print('Sorry. Zero is not a valid input. ')
        except:
            print('Sorry. That\'s not a valid input. ')