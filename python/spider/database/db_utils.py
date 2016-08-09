#!/usr/bin/python
# coding=utf8
# author: liuhanlong
# date: 16/8/6 上午12:23

import MySQLdb


class MySqlUtils:

    def __init__(self, hostname='45.114.11.43', username='mars', password='laizheli512',
                 db='mars', port=3306, charset='utf8'):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db = db
        self.port = port
        self.charset = charset
        self.conn = MySQLdb.connect(host=hostname, user=username, passwd=password, db=db, port=port, charset=charset)

    def get_cursor(self):
        cursor = self.conn.cursor()
        return cursor

    def query_all(self, query):
        cursor = self.get_cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return res
