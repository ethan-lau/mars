# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5

import MySQLdb
import MySQLdb.cursors


class MySQLStorePagePipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_insert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    def _do_insert(self, conn, item, spider):
        now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
        url_md5 = md5(item['url']).hexdigest()
        conn.execute("""select 1 from page_reference where url_md5 = %s and source = %s""", (url_md5,item['source']))
        ret = conn.fetchone()

        if not ret:
            conn.execute("""
              insert into page_reference(title, url_md5, url, source, author, update_time) values(%s,%s,%s,%s,%s,%s)
              """, (item['title'], url_md5, item['url'], item['source'], item['author'], now))

    def _handle_error(self, failure, item, spider):
        print failure, '================='
        pass

