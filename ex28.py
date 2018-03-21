#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex28.py
숫자 추가
"""


if __name__ == '__main__':
    total = 0

    for i in range(5):
        num = int(input('Enter a number: '))
        total += num

    print('The total is {}.'.format(total))
