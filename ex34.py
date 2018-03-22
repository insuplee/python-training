#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex34.py
사원 명단 삭제
"""


EMPLOYEE_LIST = [
    'John Smith',
    'Jackie Jackson',
    'Chris Jones',
    'Amanda Cullen',
    'Jeremy Goodwin'
]


# show number of employees and names of each employee
def show_employee_list():
    global EMPLOYEE_LIST

    print('There are {} employees: '.format(len(EMPLOYEE_LIST)))
    for employee in EMPLOYEE_LIST:
        print(employee)


def delete_employee(employee_name):
    global EMPLOYEE_LIST

    if employee_name in EMPLOYEE_LIST:
        # NOTE : EMPLOYEE_LIST.remove(employee_name) is also possible.
        # NOTE : using remove method, you must consider error handling
        EMPLOYEE_LIST = list(filter(lambda n: n != employee_name, EMPLOYEE_LIST))
    else:
        print('There is no \"{}\" in the employee list. '.format(employee_name))


def main():
    show_employee_list()

    # input
    employee_name = input('Enter an employee name to remove: ')

    # process
    delete_employee(employee_name)

    show_employee_list()

if __name__ == '__main__':
    main()
