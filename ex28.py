#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex28.py
add number
"""


# error handling is implemented
def add_number(num_of_numbers):
    total = 0

    for i in range(num_of_numbers):
        try:
            input_num = int(input('Enter a number: '))
            total += input_num
        except ValueError:
            pass

    return total


def main():
    # input
    try:
        num_of_numbers = int(input('Enter the number of numbers to add: '))
    except ValueError:
        print('invalid value')
        return None

    # process
    total = add_number(num_of_numbers)

    # output
    print('The total is {}.'.format(total))


if __name__ == '__main__':
    main()
