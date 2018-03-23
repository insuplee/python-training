#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex52_server.py
own alarm client
"""

import calendar
import requests


TARGET_URL = 'http://127.0.0.1:5000/time'


def process_json_current_time(target_url):
    response = requests.get(url=target_url)
    extracted_json = response.json()

    current_time = extracted_json['currentTime']

    date_info = current_time.split(' ')[0]
    time_info = current_time.split(' ')[1]

    y = int(date_info.split('-')[0])
    m = int(date_info.split('-')[1])
    d = int(date_info.split('-')[2])

    print(f'The current time is {time_info} UTC {calendar.month_name[m]} {d} {y}.')


def main():
    global TARGET_URL
    process_json_current_time(TARGET_URL)


if __name__ == '__main__':
    main()
