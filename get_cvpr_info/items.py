# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetCvprInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    paper_title = scrapy.Field()
    paper_authors = scrapy.Field()
