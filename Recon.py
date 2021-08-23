import scrapy
from scrapy.http.request import Request

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://54.169.8.122/Python/172.18.58.238/algenius/index.html'] # Website to crawl

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'} # User-Agent, change this as needed
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response):
        css_selector = 'img'
        reference = 'a'
        for j in response.css(reference):
            sel ='@href'
            yield {
                'Header': j.xpath(sel).get()
            }
        for x in response.css(css_selector):
            newsel ='@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        print(response.request.headers['User-Agent']) #Display the User-Agent in the output