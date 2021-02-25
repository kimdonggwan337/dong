# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()
    
    def process_item(self, item, spider):
        self.storeInDb(item)
        return item
    
    def storeInDb(self, item):
        created_at=item.get('time','').strip()
        trade=item.get('trade','').strip()
        price=item.get('price','').strip()
        max_price=item.get('max_price','').strip()
        min_price=item.get('min_price','').strip()
        stock_code=item.get('stock_code','').strip()
        
        sql="INSERT INTO stock_info(created_at,trade,price, max_price, min_price,stock_code) VALUES(%s,%s,%s,%s,%s,%s)"
        
    # created_at = scrapy.Field()
    # trade = scrapy.Field()
    # price = scrapy.Field()
    # max_price = scrapy.Field()
    # min_price = scrapy.Field()
    # stock_code = scrapy.Field()

        self.cur.execute(sql,(created_at,trade,price,max_price,min_price,stock_code))
        self.conn.commit()
    
    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='mydb',charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")
    
    
    def createTable(self):
        self.cur.execute("DROP TABLE IF EXISTS stock_info")
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS stock_info(
            created_at VARCHAR(100),
            trade VARCHAR(100), 
            price VARCHAR(100), 
            max_price VARCHAR(50),
            min_price VARCHAR(100),
            stock_code VARCHAR(20) PRIMARY KEY
            )''')