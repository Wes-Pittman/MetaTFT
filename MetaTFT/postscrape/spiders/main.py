import scrapy as s


class PostsSpider(s.Spider):
    name = "meta"

    def start_request(self):
        urls = [
            'https://www.metatft.com/comps',
            'https://www.metatft.com/units',
            'https://www.metatft.com/traits'

        ]
        for url in urls:
            yield s.Request(url=url, callback=self.parse)

    def parse(self, response):
        for comp in response.css('div.CompRow1'):
            yield {
                'comp': comp.css('div.tags a.tag::text')
            }
