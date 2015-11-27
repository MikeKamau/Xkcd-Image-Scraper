from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from scrapy.http.request import Request
from xkcd.items import XkcdItem

class MySpider(CrawlSpider):
	name = "xkcd"
	allowed_domains = ["xkcd.com"]
	start_urls = ["http://xkcd.com/1/"]

	rules = (
		
     	Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@rel="next"]',)), callback="parse_image", follow= True),
	)

	def parse_image(self, response):
		image = XkcdItem()
		image['title'] = response.xpath('//div[@id="ctitle"]/text()').extract()[0]
		rel_url = response.xpath('//div[@id="comic"]/img/@src').extract()[0]
		image['image_urls'] = ['http:' + rel_url]
		return image
		
