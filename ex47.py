#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex47.py
who is on space?
"""

import requests
import myutil


TARGET_URL = 'http://api.open-notify.org/astros.json'


def process_json_people_list(target_url):
    response = requests.get(url=target_url)

    extracted_json = response.json()

    people_list = extracted_json['people']

    # widths are used for prettier print
    width1 = max(list(map(lambda x: len(x['name']), people_list)))
    width2 = max(list(map(lambda x: len(x['craft']), people_list)))

    # output
    myutil.print_row(['Name', 'Craft'], [width1, width2], sep=' | ')
    myutil.print_row(['-' * width1, '-' * width2], [width1, width2], sep='-|-')
    for person in people_list:
        myutil.print_row([person['name'], person['craft']], [width1, width2], sep=' | ')


def main():
    global TARGET_URL
    process_json_people_list(TARGET_URL)


if __name__ == '__main__':
    main()
