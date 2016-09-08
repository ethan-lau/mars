# -*- coding: utf-8 -*-
import scrapy
from PageCrawl.items import BlogItem

class CnblogsSpider(scrapy.Spider):
    name = "cnblogs"
    allowed_domains = ["cnblogs.com"]
    start_urls = (
        'http://www.cnblogs.com/pick',
    )

    def parse(self, response):
        page_list = response.xpath('//div[@id="post_list"]/div[@class="post_item"]')
        for page in page_list:
            item = BlogItem()
            item['url'] = page.css('div.post_item_body>h3>a::attr(href)').extract()[0]
            item['title'] = page.css('div.post_item_body>h3>a::text').extract()[0]
            item['author'] = page.css('div.post_item_foot>a::text').extract()[0]
            item['source'] = 'cnblogs'
            yield item