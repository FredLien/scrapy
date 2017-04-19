# -*- coding: utf-8 -*-
import scrapy
from book_sale.items import BookSaleItem


class KoboSpider(scrapy.Spider):
	name = "kobo"
	allowed_domains = ["https://www.kobo.com/tw/zh"]
	start_urls = ['https://www.kobo.com/tw/zh']

	def parse(self, response):

		item = BookSaleItem()
		top_node = reponse.xpath('//section[@id="99"]')
		key_url = './div/div/a/div/text()'
		value_url = ''
		sale = u'今日99'

		if top_node.xpath(key_url).extract_first() == sale:
			print top_node.xpath()
