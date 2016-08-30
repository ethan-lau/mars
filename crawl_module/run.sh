#!/bin/sh

export APP_HOME=`dirname $0;`

cd $APP_HOME/PageCrawl
# scrapy crawl oschina
scrapy crawl cnblogs
