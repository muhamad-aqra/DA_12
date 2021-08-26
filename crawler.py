import scrapy 
from scrapy.http.request import Request
import requests

#Q5

url = 'https://brickset.com/sets/year-2009'
r = requests.get(url) #GET REQUEST
h = requests.head(url)
print('GET REQUEST', r.text) #show get request output
input('Hold...')
print('Status Code:')
print('OK', r.status_code)
input('Hold...')
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
input('Hold...')
url2 = 'http://httpbin.org/headers'
headers = {
    'User-Agent' : 'Mobile'
}
rh = requests.get(url2, headers=headers)
print(rh.text)
input('Hold...')

#Q6
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://brickset.com/sets/year-2009']

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'} #header for initial url
        for url in self.start_urls:
            yield Request(url, headers=headers)


#Q7
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
        Page_selector = '.next a ::attr(href)' #To recurse next page
        next_page = response.css(Page_selector).extract_first()
        headers = {'User-Agent': 'Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0'} #header for recurved paged
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback = self.parse,
                headers=headers
        )
