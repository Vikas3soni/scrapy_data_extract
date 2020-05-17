#recommended to install scrapy in virtual enviroment using below command:
>> pip install scrapy

#check scrapy version
>> scrapy version

#Create scrapy basic project structure
>> scrapy startproject myproject [project_dir]
  Structure details::
  ==>project_dir
      ==> scrapy.cfg
      ==> myproject
              ==> __init__.py
              ==> items.py
              ==> pipelines.py
              ==> middlewares.py
              ==> settings.py
              ==> spiders
                 ==> __init__.py

## Check avaliable templates for spider
>> scrapy genspider -l

##Syntax to create spider:
>> scrapy genspider [-t template] <name> <domain>

## Created spider name 'example' using template 'basic'
>> scrapy genspider example example.com

##Created spider name 'scrapyorg' using template 'crawl'
>> scrapy genspider -t crawl scrapyorg scrapy.org

## get spider list
>> scrapy list

##Check spider details
>> scrapy check [-l] <spider>

#Edit any spider content
>> scrapy edit spider1

#fetch url fromm commandline
>> scrapy fetch <url>
or
>> scrapy fetch --nolog <url>
or
>> scrapy url <url>

#vew url through brower:
>> scrapy view <url>

##Access settings keys:
Syntax: >> scrapy settings --get <key_name>
>> scrapy settings --get BOT_NAME


## Run a spider self-contained in a Python file, without having to create a project.
>> scrapy runspider <spider_file.py>


