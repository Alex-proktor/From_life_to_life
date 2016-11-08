#!/usr/bin/env python
# coding=utf-8

import socket
PORT = 9090              # Arbitrary non-privileged port

sock = socket.socket()
sock.connect(('localhost', PORT))   # подключение к серверу
sock.send('wasdfsdf')

data = sock.recv(1024)
sock.close()

print data

