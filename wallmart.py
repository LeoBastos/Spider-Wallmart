import scrapy
import json


class WallmartSpider(scrapy.Spider):
    name = 'Wallmart'

    custom_settings = {
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'AUTOTHROTTLE_ENABLED': True
        #'AUTOTHROTTLE_START_DELAY': 10
    }

    def start_requests(self):
        #'https://www.walmart.com/search?q=notebook%20acer'
        'https://www.walmart.com/search?q=notebook+acer&page=25&affinityOverride=default'

        for page in range(1, 26):
            yield scrapy.Request(f'https://www.walmart.com/search?q=notebook+acer&page={page}&affinityOverride=default')

    def parse(self, response, **kwargs):
        html = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        results = html.get('props').get('pageProps').get('initialData').get('searchResult').get('itemStacks')[0].get('items')
        for result in results:
            yield{
                'name': result.get('name'),
                'ratting': result.get('averageRating'),
                'reviews': result.get('numberOfReviews'),
                'seller': result.get('sellerName'),
                'stock': result.get('availabilityStatusDisplayValue'),
                'price': result.get('price'),
                'images': result.get('image'),
                'url': result.get('canonicalUrl')
            }
