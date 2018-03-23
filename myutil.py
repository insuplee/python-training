#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
myutil.py
utility functions are implemented
"""


# print 'row' for better readability(prettier)
def print_row(data_list, width_list, sep=' '):
    # number of data and number of widths must be same
    assert len(data_list) == len(width_list)

    # f-strings are available since python 3.6
    result_str = f'{data_list[0]:{width_list[0]}}'

    for i in range(1, len(data_list)):
        temp_str = f'{sep}{data_list[i]:{width_list[i]}}'
        result_str += temp_str

    print(result_str)


