# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem

class IreadSpider(scrapy.Spider):
	name = "iread"
	allowed_domains = ["https://www.iread.com.tw"]
	start_urls = ['http://www.iread.com.tw']

	def parse(self, response):

		item = BookSaleItem()
		top_node = response.xpath('//div[@class="iReadbammerLeft"]')
		key_url = './div/div/span[@class="todaydiscount"]'
		value_url = './div/div[@class="chosen_wen"]/a/text()'

		if top_node.xpath(key_url):
			result = top_node.xpath(value_url).extract_first()
			self.log("Iread: %s" % result)
			item['Iread'] = result
			return item
