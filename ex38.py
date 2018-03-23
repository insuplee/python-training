#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex38.py
filter even numbers
"""


# NOTE : rename "filterEvenNumbers" to "filter_even_numbers" for consistency
def filter_even_numbers(input_str):
    tmp_arr = input_str.split(' ')
    number_arr = list(map(lambda x: int(x), tmp_arr))

    even_num_arr = []
    for number in number_arr:
        if number % 2 == 0:
            even_num_arr.append(number)

    return even_num_arr


def main():
    # input
    input_str = input('Enter a list of numbers, separated by spaces: ')

    # process
    even_number_arr = filter_even_numbers(input_str)

    # output
    print('The even numbers are ', end='')
    for even_num in even_number_arr:
        print(even_num, end=' ')


if __name__ == '__main__':
    main()

