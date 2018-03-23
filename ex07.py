#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex07.py
area of square room
"""

CONSTANT_FOR_FEET_TO_METER = 0.09290304


# convert square feet to square meters
def square_ft_to_square_mt(square_ft):
    square_mt = square_ft * CONSTANT_FOR_FEET_TO_METER
    return square_mt


# calculate square feet area by length(feet) and width(feet)
def calculate_feet_area(length_ft, width_ft) :
    return length_ft * width_ft


# calculate square meters area by length(feet) and width(feet)
def calculate_meters_area(length_ft, width_ft):
    feet_area = calculate_feet_area(length_ft, width_ft)
    meters_area = square_ft_to_square_mt(feet_area)
    return meters_area


def main():
    # input
    length_ft = int(input('What is the length of the room in feet? '))
    width_ft = int(input('What is the width of the room in feet? '))

    print('You entered dimensions of {0} feet by {1} feet'.format(length_ft, width_ft))

    # process
    feet_area = calculate_feet_area(length_ft, width_ft)
    meters_area = calculate_meters_area(length_ft, width_ft)

    # output
    print('The area is')
    print('{} square feet'.format(feet_area))
    print('{:.3f} square meters'.format(meters_area))


if __name__ == '__main__':
    main()
