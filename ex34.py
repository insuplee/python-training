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


def delete_employee():
    global EMPLOYEE_LIST

    name = input('Enter an employee name to remove: ')

    if name in EMPLOYEE_LIST:
        EMPLOYEE_LIST = list(filter(lambda n: n != name, EMPLOYEE_LIST))
    else:
        print('There is no \"{}\" in the employee list. '.format(name))


if __name__ == '__main__':
    show_employee_list()
    delete_employee()
    show_employee_list()