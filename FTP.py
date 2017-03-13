#!/usr/bin/env python
# coding=utf-8

import time
import socket
import Config

# class ftp():

    # def __init__(self):
    #     self.PORT = 9090              # Arbitrary non-privileged port
    #     self.sock = socket.socket()

def sendData(sent_data):
    PORT = 9090              # Arbitrary non-privileged port
    sock = socket.socket()

    sent_data = str(sent_data)

    sock.connect(('localhost', PORT))   # подключение к серверу
    sock.sendall(sent_data)

    time.sleep(1)

    data = sock.recv(1024)
    sock.close()

    print data
    return data

