#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex07.py
직사각형 방의 면적
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


# print areas by feet and meters
def print_area(feet_area, meters_area):
    print('The area is')
    print('{} square feet'.format(feet_area))
    print('{:.3f} square meters'.format(meters_area))


if __name__ == '__main__':
    input_length_ft = int(input('What is the length of the room in feet? '))
    input_width_ft = int(input('What is the width of the room in feet? '))
    print('You entered dimensions of {0} feet by {1} feet'.format(input_length_ft, input_width_ft))

    output_feet_area = calculate_feet_area(input_length_ft, input_width_ft)
    output_meters_area = calculate_meters_area(input_length_ft, input_width_ft)

    print_area(output_feet_area, output_meters_area)
