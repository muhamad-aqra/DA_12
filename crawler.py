import scrapy 
from scrapy.http.request import Request

class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2009']
    

    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2009']
    def parse(self, response):
                        css_selector = 'img'
                        for x in response.css(css_selector):
                                       newsel = '@src'
                                       yield {
                                                'Image Link': x.xpath(newsel).extract_first(),
                                        }
def start_request(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'}
        for url in self.start_urls:
            yield Request(url, headers=headers)



        name = "new_spider"
        start_urls = ['https://brickset.com/sets/year-2009']
        def parse(self, response):
                xpath_selector = '//img'
                for x in response.xpath(xpath_selector):
                        newsel = '@src'
                        yield {
                                'Image Link':x.xpath(newsel).extract_first(),
                        }

#To recurse next page
                Page_selector = '.next a ::attr(href)'
                next_page = response.css(Page_selector).extract_first()
                if next_page:
                        yield scrapy.Request(
                                response.urljoin(next_page),
                                callback = self.parse
                )
