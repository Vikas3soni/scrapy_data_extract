# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst, MapCompose, Join
# from w3lib.html import remove_tags
#
# def strip(value):
# 	return value.strip()
#
# class BaseItemLoader(ItemLoader):
# 	default_input_processor = MapCompose(remove_tags, strip)
# 	default_output_processor = MapCompose()
#
# class CollegeListLoader(BaseItemLoader):
#     college_name = TakeFirst()
#     college_location = TakeFirst()
#     college_url = TakeFirst()
#
