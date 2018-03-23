#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of CodeTraining
# Copyright (C) Insup Lee <dlstjq0711@naver.com>
# March 2018

"""
ex52.py
make own alarm server
"""

import socket
import time

HOST = ''
PORT = 10002


def main():
    global HOST, PORT

    print('start server... ')

    # 1.소켓을 생성한다.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.소켓 주소 정보 할당
    s.bind((HOST, PORT))
    print('bind')

    # 3.연결 수신 대기 상태
    s.listen(100)
    print('listen')

    connection_list = [s]

    while connection_list:
        try:
            # 4.연결 수락
            client_socket, addr_info = s.accept()
            connection_list.append(client_socket)
            print('accept')

            print('{} hello'.format(time.ctime()))
            client_socket.send('hello')

            # 소켓 종료
            client_socket.close()
            print('close')
        except KeyboardInterrupt:
            s.close()
            return None


if __name__ == '__main__':
    main()
