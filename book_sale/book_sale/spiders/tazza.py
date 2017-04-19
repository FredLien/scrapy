# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem


class TazzaSpider(scrapy.Spider):
	name = "tazza"
	allowed_domains = ["http://www.taaze.tw/act66.html"]
	start_urls = ['http://www.taaze.tw/act66.html']

	def parse(self, response):

		item = BookSaleItem();
		top_node = response.xpath('//table')
		key_url = './tr/td/img[@src="/include/act/img/today-66.jpg"]'
		value_url = './tr/td/table/tr/td/span[@class="txt-b"]/text()'

		# lookup the key and value
		'''
		top_node
			|
			|--- key
			|--- value
		'''
		for x in top_node:
			if x.xpath(key_url):
				result = x.xpath(value_url).extract_first()
				self.log('Tazza: %s' % result)
				item['Tazza'] = result
				return item
