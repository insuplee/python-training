#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex27.py
입력 값 검증
"""

import re


class UserInfo:
    _first_name = ''
    _last_name = ''
    _zip_code = 0
    _employee_id = ''
    _is_validation_error = False

    # set user information
    # setting process will be done automatically in constructor
    def __init__(self):
        self._first_name = input('Enter the first name: ')
        self._last_name = input('Enter the last name: ')
        self._zip_code = input('Enter the ZIP code: ')
        self._employee_id = input('Enter an employee ID: ')

    # validate user information
    # validation process will be done by method call
    # NOTE : rename "validateInput" to "validate_input" for consistency
    def validate_input(self):
        # initialize error state
        self._is_validation_error = False

        # validate each data
        self.validate_first_name()
        self.validate_last_name()
        self.validate_zip_code()
        self.validate_employee_id()

        if not self._is_validation_error:
            print('There were no errors found.')

    def validate_first_name(self):
        if len(self._first_name) == 0:
            print('The first name must be filled in.')
            self._is_validation_error = True
        elif len(self._first_name) == 1:
            print('\"{}\" is not a valid first name. It is too short.'.format(self._first_name))
            self._is_validation_error = True

    def validate_last_name(self):
        if len(self._last_name) == 0:
            print('The last name must be filled in.')
            self._is_validation_error = True
        elif len(self._last_name) == 1:
            print('\"{}\" is not a valid last name. It is too short.'.format(self._last_name))
            self._is_validation_error = True

    def validate_zip_code(self):
        # pattern : only numbers
        # example : 00 or 000 or 00000...
        pattern = r'^(\d+)$'

        # pattern matching
        if not re.search(pattern, self._zip_code):
            print('The ZIP code must be numeric.')
            self._is_validation_error = True

    def validate_employee_id(self):
        # pattern : 2 alphabets, hyphen(-), 4 numbers
        # example : AA-0000
        pattern = r'^[a-zA-Z][a-zA-Z][-](\d{4})$'

        # pattern matching
        if not re.search(pattern, self._employee_id):
            print('{} is not a valid ID.'.format(self._employee_id))
            self._is_validation_error = True


if __name__ == '__main__':
    user = UserInfo()
    user.validate_input()
