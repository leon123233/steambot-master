from scrapy.spider import Spider,BaseSpider
from scrapy.selector import Selector
from steambot.items import Website
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class SteamSpider(Spider):
    name = "steam"
    allowed_domains = ["store.steampowered.com"]
    start_urls = []
    startpage = 1
    endpage = 208
    for page in range(startpage,endpage+1):
        start_urls.append("http://store.steampowered.com/search/?sort_by=_ASC&category1=998&page=%s"%str(page))
    rules = (
        Rule(LinkExtractor(deny=(),),callback=None,follow=None,),
    )
    def __init__(self):
        binary = FirefoxBinary('./Firefox/firefox.exe')
        self.browser = webdriver.Firefox(firefox_binary=binary)
    def __del__(self):
        pass
    def parse(self, response):
        self.browser.get(response.url)
        sel = Selector(text=self.browser.page_source)
        sites = sel.xpath('//a[@class="search_result_row ds_collapse_flag"]')
        items = []
        for site in sites:
            item = Website()
            item['name'] = site.xpath('div[@class="col search_name ellipsis"]/span/text()').extract()
            item['price'] = site.xpath('div[@class="col search_price "]/text()').extract()
            if item['price'] == []:
                item['price'] = site.xpath('div[@class="col search_price discounted"]/text()').extract()
            item['price'] = [reduce(lambda x,y:"".join(x.split())+"".join(y.split()),item['price'],"")]
            item['released_day'] = site.xpath('div[@class="col search_released"]/text()').extract()
            items.append(item)
        return items
