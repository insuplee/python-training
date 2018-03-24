#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex37.py
generate password
"""

import string
import random


LOWER_CHARACTERS = list(string.ascii_lowercase)
SPECIAL_CHARACTERS = list(set(string.punctuation))
NUMBERS = list(string.digits)


def generate_password(password_len, special_char_num, numbers_num):
    global LOWER_CHARACTERS, SPECIAL_CHARACTERS

    password = ''
    for i in range(special_char_num):
        tmp_index = random.randint(0, len(SPECIAL_CHARACTERS)-1)
        password += SPECIAL_CHARACTERS[tmp_index]
    for i in range(numbers_num):
        tmp_index = random.randint(0, len(NUMBERS)-1)
        password += NUMBERS[tmp_index]

    tmp_password_len = len(password)
    for i in range(tmp_password_len, password_len):
        tmp_index = random.randint(0, len(LOWER_CHARACTERS) - 1)
        password += LOWER_CHARACTERS[tmp_index]

    password = shuffle_string(password)
    return password


# password type is <class 'str'>
def shuffle_string(password):
    tmp_list = list(password)
    random.shuffle(tmp_list)

    shuffled_password = ''.join(tmp_list)
    return shuffled_password


def main():
    # input : error handling is also implemented
    try:
        password_num = int(input('# How many passwords? '))
        password_len = int(input('> What\'s the minimum length? '))
        special_char_num = int(input('> How many special characters? '))
        numbers_num = int(input('> How many numbers? '))
    except ValueError:
        print('Error : invalid input')
        return None

    # process : generate passwords
    password_list = []
    for i in range(password_num):
        password = generate_password(password_len, special_char_num, numbers_num)
        password_list.append(password)

    # output : show all generated passwords
    print(password_list)


if __name__ == '__main__':
    main()
