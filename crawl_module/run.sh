#!/bin/sh

export APP_HOME=`dirname $0;`

cd $APP_HOME/PageCrawl
scrapy crawl oschina
#`cd /data/code/mars/PageCrawl/PageCrawl && scrapy crawl oschina`
