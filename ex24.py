#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex24.py
애너그램 점검
"""


# Although example recommends function name as isAnagram,
# I decide function's name as is_anagram because of consistency
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    # NOTE : sorted and sort are different method
    # lower() method for case-insensitive
    l1 = sorted(list(str1.lower()))
    l2 = sorted(list(str2.lower()))

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True


if __name__ == '__main__':
    print('Enter two strings and I\'ll tell you if they are anagrams: ')
    input_str1 = input('Enter the first string: ')
    input_str2 = input('Enter the second string: ')

    if is_anagram(input_str1, input_str2):
        print('\"{0}\" and \"{1}\" are anagrams'.format(input_str1, input_str2))
    else:
        print('\"{0}\" and \"{1}\" are not anagrams'.format(input_str1, input_str2))