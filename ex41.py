#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex41.py
이름 정렬
"""


FILE_NAME = 'ex41_namelist.txt'


def make_namelist_file(use_default_namelist=True):
    global FILE_NAME
    namelist = []

    if use_default_namelist:
        default_namelist = [
            'Ling, Mai',
            'Johnson, Jim',
            'Zarnecki, Sabrina',
            'Jones, Chris',
            'Jones, Aaron',
            'Swift, Geoffrey',
            'Xiong, Fong'
        ]
        namelist = default_namelist[:]
    else:
        try:
            num_of_names = int(input('Enter number of names: '))
            for i in range(num_of_names):
                name = input('Enter name(ex. Ling, Mai): ')
                namelist.append(name)
        except ValueError:
            print('Invalid Input causes ValueError. ')
            return None

    # file open for writing namelist
    file_wt = open(FILE_NAME, 'wt')

    for name in namelist:
        file_wt.write(name)
        if name != namelist[-1]:
            file_wt.write('\n')

    file_wt.close()


def read_namelist_file():
    global FILE_NAME

    file_rt = open(FILE_NAME, 'rt')

    tmp_str = file_rt.read()
    extracted_namelist = tmp_str.split('\n')
    file_rt.close()

    # process : sort by alphabet sequence
    extracted_namelist.sort()
    num_of_names = len(extracted_namelist)

    # max_name_len is used for readability
    max_name_len = max(list(map(lambda x: len(x), extracted_namelist)))

    # output
    print('Total of {} names'.format(num_of_names))
    print('-' * max_name_len)
    for name in extracted_namelist:
        print(name)


def main():
    # make_namelist_file(use_default_namelist=False) is also possible
    make_namelist_file()

    # process & output
    read_namelist_file()

if __name__ == '__main__':
    main()
