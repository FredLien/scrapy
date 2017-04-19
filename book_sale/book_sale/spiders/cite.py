# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem

class CiteSpider(scrapy.Spider):
	name = "cite"
	allowed_domains = ["http://www.cite.com.tw"]
	start_urls = ['http://www.cite.com.tw']

	def parse(self, response):

		sale = u'66折價'
		item = BookSaleItem()
		top_node = response.xpath('//ul[@class="box"]')
		key_url = './li/a/span/text()'
		value_url = './li[@class="center"]/text()'

		if top_node.xpath(key_url).re_first(sale) == sale:
			result = top_node.xpath(value_url).extract_first()
			self.log('Cite: %s' % result)
			item['Cite'] = result
			return item
