#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex46.py
count word-frequency
"""

import myutil


FILE_NAME = 'ex46_wordlist.txt'


def count_word_frequency(file_name):
    with open(file_name, "rt") as f:
        tmp_data = f.read()

    word_list = tmp_data.replace('\n', ' ').split(' ')

    word_dict_keys = list(set(word_list))

    # create dictionary based on word_list
    word_dict = dict()

    for key in word_dict_keys:
        word_dict[key] = word_list.count(key)

    # sort by dictionary value : number of frequency
    sorted_wd_list = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    # widths are used for prettier print
    width1 = max(list(map(lambda x: len(x[0]), sorted_wd_list)))
    width2 = max(list(map(lambda x: x[1], sorted_wd_list)))

    # output
    for word_info in sorted_wd_list:
        # 1 in (width + 1) means length of ':'
        myutil.print_row([word_info[0] + ':', '*' * word_info[1]], [width1+1, width2+1], sep=' ')


def main():
    global FILE_NAME
    count_word_frequency(FILE_NAME)


if __name__ == '__main__':
    main()
