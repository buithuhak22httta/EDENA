import scrapy


class ItemSpider(scrapy.Spider):
    name = "items"

    def start_requests(self):
        urls = [
            'https://edena.vn/collections/chan-ra-goi/',
            'https://edena.vn/collections/nem/',
            'https://edena.vn/collections/ruot-goi',
            'https://edena.vn/collections/topper-edena',
            'https://edena.vn/collections/edena-basic'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        list_item = response.css('div.product-info')
        for item in list_item:
            res = scrapy.Request(url='https://edena.vn'+item.xpath('a/@href').get(), callback=self.parse_product)           
            yield res
                #'item': item.css('h3.product-title::text').get(),
                

    def parse_product(self, response): 
        #options = response.xpath('//select[@id="product-select"]/option/text()').getall()
        yield {
        'list' : response.xpath('//select[@id="product-select"]/option/text()').getall(),
        }
    
    