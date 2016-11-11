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

class check_events():
    def __init__(self):
        self.filename = 'setting.cfg'
        self.cfgParser = ConfigParser.RawConfigParser()
        self.cfgParser.read(self.filename)
    def setGameActive(self, events_value):
        self.cfgParser.set('check_events', 'game_active', str(events_value))
        self.cfgParser.write(open(self.filename, 'wb'))
    def getGameActive(self):
        return self.cfgParser.get('check_events', 'game_active')
