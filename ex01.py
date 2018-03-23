#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex01.py
greeting
"""


def greeting(name):
    print('Hello, {0}, nice to meet you!'.format(name))


def main():
    # input
    name = input('What is your name? ')

    # output
    greeting(name)


if __name__ == '__main__':
    main()
