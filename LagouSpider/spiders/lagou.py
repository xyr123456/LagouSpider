# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow=("zhaopin/.*,")),follow=True),
        Rule(LinkExtractor(allow=("gongsi/j\d+.html,")),follow=True),
        Rule(LinkExtractor(allow=r'jobs/\d+.html'), callback='parse_job', follow=True),
    )

    #重写方法模拟登录
    def start_requests(self):
        #去使用selenium模拟登录后拿到cookie交给scrapy的request使用
        from selenium import webdriver
        brower=webdriver.Chrome()



    def parse_job(self, response):
        #解析拉勾网的职位
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
