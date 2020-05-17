# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
#[Extract Data] ==> [Temporary container(Item)] ==> Storing in database
import scrapy


class CollegeListItem(scrapy.Item):
    college_name = scrapy.Field()
    college_location = scrapy.Field()
    college_url = scrapy.Field()

class CollegeDetailItem(scrapy.Item):
    former_name = scrapy.Field()
    students = scrapy.Field()
    location = scrapy.Field()
    undergraduates = scrapy.Field()
    postgraduates = scrapy.Field()
