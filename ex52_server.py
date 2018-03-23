#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex52_server.py
own alarm server
"""

import json
import datetime
from flask import Flask, render_template, redirect, Response


# name of global variables are recommended to be CAPITAL.
# 'app' in this case is exception.
app = Flask(__name__)
MAIN_PAGE_HTML = 'ex52_mainpage.html'
ERROR_PAGE_HTML = 'ex52_404page.html'


@app.route('/')
def redirect_to_main():
    return redirect('http://127.0.0.1:5000/main')


# error handler has parameters
@app.errorhandler(404)
def error_404_page(e):
    global ERROR_PAGE_HTML
    return render_template(ERROR_PAGE_HTML)


@app.route('/main')
def main_page():
    global MAIN_PAGE_HTML
    return render_template(MAIN_PAGE_HTML)


@app.route('/time')
def time_page():
    current_time = str(datetime.datetime.now()).split('.')[0]

    time_dict = dict()
    time_dict['currentTime'] = current_time

    # convert time information dictionary to json format
    current_time_json = json.dumps(time_dict)

    return Response(current_time_json, content_type='application/json')


def main():
    global app
    app.run()


if __name__ == '__main__':
    main()



