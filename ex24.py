#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex24.py
애너그램 점검
"""


# NOTE : rename "isAnagram" to "is_anagram" for consistency
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


def main():
    # input
    print('Enter two strings and I\'ll tell you if they are anagrams: ')
    str1 = input('Enter the first string: ')
    str2 = input('Enter the second string: ')

    # process & output
    if is_anagram(str1, str2):
        print('\"{0}\" and \"{1}\" are anagrams'.format(str1, str2))
    else:
        print('\"{0}\" and \"{1}\" are not anagrams'.format(str1, str2))

if __name__ == '__main__':
    main()
