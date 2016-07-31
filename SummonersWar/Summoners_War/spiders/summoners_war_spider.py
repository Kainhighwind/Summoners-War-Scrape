import scrapy
from Summoners_War.items import SummonersWarItem

class SummonersWarSpider(scrapy.Spider):
    name = "summoners_war"
    allowed_domains = ["http://summonerswar.wikia.com"]
    start_urls = [
        "http://summonerswar.wikia.com/wiki/Fire_Monsters"
    ]

    '''def parse(self, response):
        for sel in response.xpath('//a[@class="mw-redirect"]'):
            item = SummonersWarItem()
            item['monster_page'] = sel.xpath('a/@href').extract()
            item['monster_name'] = sel.xpath('a/text()').extract()#puts all the monster names (from the links) into the 'monster_name' element of the Item
            yield item
                '''

    def parse(self, response):
        monsters = response.xpath('//a[@class="mw-redirect"]')
        for monsters in monsters:
            item = SummonersWarItem()
            item['monster_page'] = monsters.xpath('/@href').extract()
            item['monster_name'] = monsters.xpath('/text()').extract()  # puts all the monster names (from the links) into the 'monster_name' element of the Item
            yield item