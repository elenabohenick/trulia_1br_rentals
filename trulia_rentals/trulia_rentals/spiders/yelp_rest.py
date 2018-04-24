import scrapy
import pandas as pd
import numpy as np
import json
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from collections import defaultdict

class YelpSpider(scrapy.Spider):
    name = 'yelp_rest'

    custom_settings = {
        "DOWNLOAD_DELAY": 2,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 5,
        "HTTPCACHE_ENABLED": True
    }

    with open("../trulia_rentals/yelp_total_rest.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]


    def __init__(self):
        chromedriver = "/Applications/chromedriver" # path to the chromedriver executable
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome()


    def parse(self, response):
        self.driver.get(response.url)
        driver.get(url)
        # get total number of restaurants
        total_rest_loc = '//span[contains(text(),"Showing 1")]'
        total_rest_raw = driver.find_element_by_xpath(total_rest_loc).text
        total_rest = int(re.sub(r'Showing 1.*of\s','',total_rest_raw))

        button1 = driver.find_element_by_xpath('//span[@class="filter-label filters-toggle js-all-filters-toggle show-tooltip"]')
        button1.click()
        time.sleep(1)

        button2 = driver.find_element_by_xpath('//span[contains(text(),"Walking (1 mi.)")]')
        button2.click()
        time.sleep(4)

        rest_num_loc = '//span[contains(text(),"Showing 1")]'
        rest_num_raw = driver.find_element_by_xpath(rest_num_loc).text
        rest_num = int(re.sub(r'Showing 1.*of\s','',rest_num_raw))

        if total_rest==rest_num:

            button3 = driver.find_element_by_xpath('//span[contains(text(),"Biking (2 mi.)")]')
            button3.click()
            time.sleep(4)

            button4 = driver.find_element_by_xpath('//span[contains(text(),"Walking (1 mi.)")]')
            button4.click()
            time.sleep(4)

            rest_num_loc = '//span[contains(text(),"Showing 1")]'
            rest_num_raw = driver.find_element_by_xpath(rest_num_loc).text
            rest_num = int(re.sub(r'Showing 1.*of\s','',rest_num_raw))


            except:
                break

        self.driver.close()


        yield {
            'url': url,
            'rest_num': rest_num_clean}
