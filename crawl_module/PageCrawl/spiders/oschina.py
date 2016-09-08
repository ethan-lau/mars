# -*- coding: utf-8 -*-
import scrapy
from PageCrawl.items import BlogItem


class OsChinaSpider(scrapy.Spider):
    name = "oschina"
    allowed_domains = ["oschina.net"]
    start_urls = (
        # 'http://www.oschina.net/blog', # 最新博客
        'http://www.oschina.net/blog/more?p=2', # 最新推荐博客
    )

    def parse(self, response):
        page_list = response.xpath('//div[@id="RecentBlogs"]/ul[@class="BlogList"]/li')
        for page in page_list:
            item = BlogItem()
            item['url'] = page.css('h3>a::attr(href)').extract()[0]
            item['title'] = page.css('h3>a::text').extract()[0]
            item['icon'] = page.css('a.u>img::attr(src)').extract()[0]
            item['author'] = page.css('a.u>img::attr(title)').extract()[0]
            item['icon'] = page.css('img.SmallPortrait::attr(src)').extract()[0]
            item['source'] = 'oschina'
            yield item
