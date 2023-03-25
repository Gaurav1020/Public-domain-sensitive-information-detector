import scrapy
from scrapy.crawler import CrawlerProcess
# from twisted.internet import reactor
import csv
import os

path=os.getcwd()
path=path.replace("\\","/")
path=path.rsplit('/',1)[0]
path=path.rsplit('/',1)[0]
path_csvfile=path+"/webspider.csv"
# print (path_csvfile)
if os.path.exists(path_csvfile):
    os.remove(path_csvfile)


class Scripts_Item(scrapy.Item):    
    Script= scrapy.Field()
    Link= scrapy.Field()
    # Script1= scrapy.Field()
    pass

items=Scripts_Item()

class PostsSpider(scrapy.Spider):
    name= "posts"
    start_urls=["http://localhost:8009/"]

    # start_urls=["http://geeksforgeeks.org/"]

    def parse(self, response):
        # yield {'SCRIPT_LINKS': response.css('script::attr(src)').getall()}
        # yield {'SCRIPT': response.css('script::text').getall()}
        leads= response.css('script::attr(src)').getall()
        for i in response.css('script::text').getall():
            items['Script']=i
            items['Link']= response.request.url
            yield items

        for i in response.css('script::attr(src)').getall():
            yield response.follow(i,callback=self.depthcrawler)


    def depthcrawler(self,response):
        items['Script']=response.css('body').get()
        items['Link']= response.request.url
        yield items


WebSpider_crawler_process = CrawlerProcess({
    'FEED_FORMAT': 'csv', 
    'FEED_URI': '../../webspider.csv',
})


WebSpider_crawler_process.crawl(PostsSpider)
WebSpider_crawler_process.start()