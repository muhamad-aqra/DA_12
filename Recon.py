import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://brickset.com/sets/year-2019'] # Website to crawl

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel ='@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }