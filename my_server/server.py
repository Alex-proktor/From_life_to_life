#!/usr/bin/env python
# coding=utf-8

"""
Принимает соединение, принимает от клиента данные,
возвращает их в виде строки в верхнем регистре и закрывает соединение.
"""

import time
import socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9090              # Arbitrary non-privileged port
client = False
conn = ''
addr = ''

def search_client():
    global client
    global conn
    global addr

    sock = socket.socket()
    sock.bind((HOST, PORT))   # хост, порт
    # print u'Сервер запущен. HOST: {0}, PORT: {1}'.format(HOST, PORT)
    sock.listen(1)  # размер очереди
    conn, addr = sock.accept()  # новый сокет и адрес клиента


    if addr:
        client = True
        # print 'connected:', addr
    else:
        client = False
    return client

# search_client()

while True:
    if search_client(): # Клиент найден
        print "search client:",  addr
        data = conn.recv(1024)  # читаем порциями по 1024 байт (или 1 кб)
        if not data:
            print(u"Нет данных")
            # break
        conn.send(data.upper()) # возвращает в виде строки в верхнем регистре
    else:
        search_client()

    time.sleep(1)

conn.close()    # закрываем соединение



# def user(name):
#     if name == "1":
#         return "Name - 1"
#     else:
#         return "No name"