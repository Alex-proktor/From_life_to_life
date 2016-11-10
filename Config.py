#!/usr/bin/env python
# coding=utf-8

import ConfigParser

class server_connection():
    def __init__(self):
        self.filename = 'setting.cfg'
        self.cfgParser = ConfigParser.RawConfigParser()
        self.cfgParser.read(self.filename)
    def getPORT(self):
        return self.cfgParser.get('server_connection','PORT')
    def getLogin(self):
        return self.cfgParser.get('server_connection','username')
    def getPass(self):
        return self.cfgParser.get('server_connection','password')
    def getTime(self):
        return self.cfgParser.get('server_connection','Time')
