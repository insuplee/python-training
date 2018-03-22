#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex14.py
세금 계산기
"""


TAX = 0.055


def calculate_tax(order_amount, state):
    tax = TAX * order_amount
    total = order_amount + tax

    if state == 'WI':
        print('The subtotal is ${:.2f}'.format(order_amount))
        print("The tax is ${:.2f}".format(tax))

    print("The total is ${:.2f}".format(total))


def main():
    # input
    order_amount = float(input('What is the order amount? '))
    state = input('What is the state? ')

    # process & output
    calculate_tax(order_amount, state)

if __name__ == '__main__':
    main()
