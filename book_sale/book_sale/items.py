# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookSaleItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	Book = scrapy.Field()
	Tazza = scrapy.Field()
	Sanmin = scrapy.Field()
	Iread = scrapy.Field()
	Cite = scrapy.Field()
