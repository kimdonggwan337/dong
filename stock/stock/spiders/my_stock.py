import scrapy
from stock.items import StockItem

class MyStockSpider(scrapy.Spider):
    name = 'my_stock'
    allowed_domains = ['finance.naver.com/item/sise.nhn?code=005930']
    start_urls = ['http://finance.naver.com/item/sise.nhn?code=005930']

    def parse(self, response):
        times = response.xpath('//*[@id="time"]/em/text()').extract()
        trades = response.xpath('//*[@id="_quant"]/text()').extract()
        prices = response.xpath('//*[@id="_nowVal"]/text()').extract()
        max_prices = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[8]/td[1]/span/text()').extract()
        min_prices = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[9]/td[1]/span/text()').extract()
        stock_codes = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()

        items = []
        for idx in range(len(stock_codes)):
            item = StockItem()
            item['time'] = times[idx]
            item['trade'] = trades[idx]
            item['price'] = prices[idx]
            item['max_price'] = max_prices[idx]
            item['min_price'] = min_prices[idx]
            item['stock_code'] = stock_codes[idx]
            items.append(item)
        return items