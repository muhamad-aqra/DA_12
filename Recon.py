import scrapy
from scrapy.http.request import Request

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019'] # Website to crawl

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'} # User-Agent, change this as needed
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel ='@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }