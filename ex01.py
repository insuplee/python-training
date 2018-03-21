#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex01.py
인사하기
"""


def print_name(name):
    print('Hello, {0}, nice to meet you!'.format(name))


if __name__ == '__main__':
    input_name = input('What is your name? ')
    print_name(input_name)