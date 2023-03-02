from scrapy.spiders import Spider

from paper_spider.items import paper_spiderItem


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        item = paper_spiderItem()
        for title in titles:
            print(title.strip())
            item["title"] = title
            return item