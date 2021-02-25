# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = scrapy.Field()
    trade = scrapy.Field()
    price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    stock_code = scrapy.Field()
