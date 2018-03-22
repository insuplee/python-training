#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex46.py
단어 빈도 탐색
"""


FILE_NAME = 'ex46_wordfile.txt'


def count_word_frequency(file_name):
    with open(file_name, "rt") as f:
        tmp_data = f.read()

    word_list = tmp_data.replace('\n', ' ').split(' ')

    # create dictionary based on word_list
    word_dict = dict()
    for word in word_list:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    # sort by dictionary value : number of frequency
    sorted_wd = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    # max_word_len is used for readability(prettier print)
    max_word_len = max(list(map(lambda x: len(x[0]), sorted_wd))) + 1
    for word_info in sorted_wd:
        print('{word_name}:{space}{word_frequency}'.format(
            word_name=word_info[0],
            space=' ' * (max_word_len - len(word_info[0])),
            word_frequency='*' * word_info[1]
        ))


def main():
    global FILE_NAME

    count_word_frequency(FILE_NAME)

if __name__ == '__main__':
    main()
