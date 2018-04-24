import scrapy
import re

class TruliaNYCSpider(scrapy.Spider):
    name = 'rentals_nyc'

    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 5,
        "HTTPCACHE_ENABLED": True
    }

    start_urls = ["https://www.trulia.com/for_rent/New_York,NY/1_beds/",
    "https://www.trulia.com/for_rent/Brooklyn,NY/1_beds/",
    "https://www.trulia.com/for_rent/Queens,NY/1_beds/",
    "https://www.trulia.com/for_rent/Bronx,NY/1_beds/",
    "https://www.trulia.com/for_rent/Staten_Island,NY/1_beds/"
    ]

    def parse(self, response):

        for href in response.xpath('//a[@class="tileLink phm"]/@href').extract():

            yield scrapy.Request(
                url="https://www.trulia.com" + href,
                callback=self.parse_listing,
                meta={'url':href,
                      'full_url': "https://www.trulia.com" + href,
                      'zipcode':href.split("-")[-3]}
            )

        next_url = response.xpath('//html//div[@class="txtC"]/a[1]/@href').extract_first()


        yield scrapy.Request(
        url = next_url,
        callback= self.parse
        )

    def parse_listing(self, response):

        url = response.request.meta['url']
        zip_code = response.request.meta['zipcode']

        parsed_link = url.split('/')[-1]
        zip_code = parsed_link.split("-")[-3]

        address_raw = response.xpath('//div[@class="mediaBody h7 ptl prxl prxxl"]/text()').extract_first()
        address_string = address_raw.split('.')[0]
        address = re.sub(r"^\n.*is located at ","",address_string)

        price_raw = response.xpath('//span[@class="h3 typeEmphasize"]/text()').extract_first()
        price = price_raw.replace('\n','').strip()

        sqft_raw = response.xpath('//ul[@id="property_features"]//li[contains(.,"sqft")]/text()').extract_first()
        if sqft_raw is not None:
            sqft = sqft_raw.replace(' sqft','')
        else:
            sqft = None

        elementary_school_count_raw = response.xpath('//p[@class="h7 typeLowlight mvn"][contains(.,"Elementary Schools")]/text()').extract_first()
        elementary_school_count = elementary_school_count_raw.replace(' Elementary Schools','')

        middle_school_count_raw = response.xpath('//p[@class="h7 typeLowlight mvn"][contains(.,"Middle Schools")]/text()').extract_first()
        middle_school_count = middle_school_count_raw.replace(' Middle Schools','')

        high_school_count_raw = response.xpath('//p[@class="h7 typeLowlight mvn"][contains(.,"High Schools")]/text()').extract_first().replace(' High Schools','')
        high_school_count = high_school_count_raw.replace(' High Schools','')

        pets_allowed_raw = response.xpath('//li[@class="iconDog"]/text()').extract_first()
        pets_allowed = pets_allowed_raw.replace('/n','').strip()

        days_on_trulia_raw = response.xpath('//li[@class="iconClock"]/text()').extract_first()
        days_on_trulia = days_on_trulia_raw.replace(' days on Trulia','').strip()

        apt_features = response.xpath('//ul[@class="mbn"]/li/text()').extract() + response.xpath('//ul[@class="mtn"]/li/text()').extract()
        if not apt_features:
            apt_features = response.xpath('//ul[@class="list2cols"]/li/text()').extract()


        yield {
            'url': url,
            'zip_code': zip_code,
            'address': address,
            'price': price,
            'sqft': sqft,
            'elementary_school_count': elementary_school_count,
            'middle_school_count': middle_school_count,
            'high_school_count': high_school_count,
            'pets_allowed': pets_allowed,
            'days_on_trulia': days_on_trulia,
            'apt_features': apt_features}
