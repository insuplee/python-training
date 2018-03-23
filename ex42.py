#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex42.py
data file parsing
"""

import myutil


FILE_NAME = 'ex42_datafile.csv'


def parsing_csv_file(file_name):
    with open(file_name, "rt") as f:
        # f.read().splitlines() is different from f.readlines()
        # in that prior thing removes newline('\n')
        namelist = f.read().splitlines()

    parsed_list = list(map(lambda x: x.split(','), namelist))

    # widths are used for prettier print
    width1 = max(list(map(lambda x: len(x[0]), parsed_list)))
    width2 = max(list(map(lambda x: len(x[1]), parsed_list)))
    width3 = max(list(map(lambda x: len(x[2]), parsed_list)))

    # output
    myutil.print_row(['Last', 'First', 'Salary'], [width1, width2, width3], sep=' ')
    myutil.print_row(['-' * width1, '-' * width2, '-' * width3], [width1, width2, width3], sep='-')
    for parsed_data in parsed_list:
        myutil.print_row([parsed_data[0], parsed_data[1], parsed_data[2]], [width1, width2, width3], sep=' ')


def main():
    global FILE_NAME

    parsing_csv_file(FILE_NAME)


if __name__ == '__main__':
    main()
