from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    price = Field()
    released_day = Field()
