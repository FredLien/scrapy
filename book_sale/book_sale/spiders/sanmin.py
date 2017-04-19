# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem


class SanminSpider(scrapy.Spider):
	name = "sanmin"
	allowed_domains = ["http://m.sanmin.com.tw/home/index.html"]
	start_urls = ['http://m.sanmin.com.tw/home/index.html']

	def parse(self, response):

		item = BookSaleItem()
		top_node = response.xpath('//li/ul')
		key_url = './li/img[@src="//m.sanmin.com.tw/images/nothing.png"]' 
		value_url = './li/table/tr/td[@class="blue13"]/a/text()'

		if top_node.xpath(key_url):
			result = top_node.xpath(value_url).extract_first()
			self.log('Sanmin: %s' % result)
			item['Sanmin'] = result
			return item

