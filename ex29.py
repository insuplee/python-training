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


def main():
    while True:
        try:
            r = int(input('What is the rate of return? '))
            years = math.ceil(72 / r)
            print('It will take {} years to double your initial investment. '.format(years))
            break
        except ZeroDivisionError:
            print('Sorry. Rate 0 causes ZeroDivision error. ')
        except ValueError:
            print('Sorry. That\'s not a valid input. ')

if __name__ == '__main__':
    main()