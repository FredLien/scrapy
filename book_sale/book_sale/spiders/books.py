# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem
from scrapy.loader import ItemLoader

class BooksSpider(scrapy.Spider):
	name = "books"
	allowed_domains = ["http://www.books.com.tw"]
	start_urls = ['http://www.books.com.tw']


	def parse(self, response):

		item = BookSaleItem()
		key = u'今日66折'
		key_url = '//div[@class="box first"]/h3/text()'
		value_url = '//div[@class="box first"]/div[@class="bd"]/h4/a/text()'

		print "Fred"
		parse_key = response.xpath(key_url).extract()[0]
		if key == parse_key:
			value = response.xpath(value_url).extract()[0]
			self.log('Book: %s' % value)
			item['Book'] = value

		return item
