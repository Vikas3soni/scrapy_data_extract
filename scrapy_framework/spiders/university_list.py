import scrapy
from ..items import CollegeListItem, CollegeDetailItem
import re

class UniversityListSpider(scrapy.Spider):
    name = 'university_list'
    allowed_domains = ['https://en.wikipedia.org/wiki/']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_universities_in_England']
    # custom_settings = {
    #     'CONCURRENT_REQUESTS': 200,
    #     'DOWNLOAD_DELAY': '0.25',
    #     'COOKIES_ENABLED': False,
    # }
    def parse(self, response):
        collegelist_item = CollegeListItem()
        row_objects = response.xpath("//table[contains(@class,'wikitable "
                                      "sortable')]//tr")

        for row_object in row_objects[1:]:
            college_location = row_object.xpath('td[2]/a/text()').extract_first(default='') + \
                               row_object.xpath('td[2]/text()').extract_first(default='')
            # if 'london' in college_location.lower():
            collegelist_item['college_location'] = re.sub('[\n,]', '',college_location)
            collegelist_item['college_name'] = re.sub('[\n,]', '', row_object.xpath("td["
                                                                                    "1]/a/text()").extract_first())
            collegelist_item['college_url'] = re.sub('[\n,]', '',  row_object.xpath("td["
                                                                                    "1]/a/@href").extract_first())
            yield response.follow(collegelist_item['college_url'],
                                  callback=self.parse_college_details)
            yield collegelist_item


    def parse_college_details(self, response):
        print("inside parse function")
        # college_name = response.xpath('//h1/text()').get()
        # print("got college_name", college_name)
        collegedetail_item = CollegeDetailItem()
        collegedetail_item['former_name'] = ''
        collegedetail_item['students'] = ''
        collegedetail_item['location'] = ''
        collegedetail_item['undergraduates'] = ''
        collegedetail_item['postgraduates'] = ''

        yield collegedetail_item

