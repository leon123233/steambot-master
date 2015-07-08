# Scrapy settings for dirbot project

SPIDER_MODULES = ['steambot.spiders']
NEWSPIDER_MODULE = 'steambot.spiders'
DEFAULT_ITEM_CLASS = 'steambot.items.Website'

ITEM_PIPELINES = {'steambot.pipelines.FilterWordsPipeline': 1}
