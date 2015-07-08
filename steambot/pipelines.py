from scrapy.exceptions import DropItem
from scrapy import signals
import json
import codecs

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""
    def __init__(self):
        self.file = codecs.open('steamgames.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
