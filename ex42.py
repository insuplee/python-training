#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex42.py
데이터 파일 파싱
"""


FILE_NAME = 'ex42_datafile.csv'


def parsing_csv_file(file_name):
    with open(file_name, "rt") as f:
        # f.read().splitlines() is different from f.readlines()
        # in that prior thing removes newline('\n')
        namelist = f.read().splitlines()

    parsed_list = list(map(lambda x: x.split(','), namelist))

    # column_lens are used for prettier print
    column1_len = max(list(map(lambda x: len(x[0]), parsed_list))) + 1
    column2_len = max(list(map(lambda x: len(x[1]), parsed_list))) + 1
    column3_len = max(list(map(lambda x: len(x[2]), parsed_list))) + 1

    # TODO : make integrated function for print, using column_lens as parameters
    print('Last{0}First{1}Salary{2}'.format(
        ' ' * (column1_len-len('Last')),
        ' ' * (column2_len-len('First')),
        ' ' * (column3_len-len('Salary'))
    ))
    print('-' * (column1_len + column2_len + column3_len))

    for parsed_data in parsed_list:
        print('{0}{1}{2}{3}{4}{5}'.format(
            parsed_data[0],
            ' ' * (column1_len - len(parsed_data[0])),
            parsed_data[1],
            ' ' * (column2_len - len(parsed_data[1])),
            parsed_data[2],
            ' ' * (column3_len - len(parsed_data[2]))
        ))


def main():
    global FILE_NAME

    parsing_csv_file(FILE_NAME)

if __name__ == '__main__':
    main()
