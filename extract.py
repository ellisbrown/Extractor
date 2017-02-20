# extract.py
# ----------
# Ellis Brown

"""
Uses selenium and chromium webdriver to extract page information from javascript loaded sites
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

# load config.ini
config = configparser.ConfigParser()
config.read('config.ini')
chromedriver = config['chromedriver']

class Extractor(object):

    def __init__(self):
        """
        calls the reinitialize method to set up the class
        """
        self.reinitialize()

    def reinitialize(self):
        """
        initializes a chromedriver instance and  a base url
        gets the url and waits for the js on the page to load
        """
        chrome_options = Options()
        args = chromedriver['args'].split(',') # args should be comma delimited
        for arg in args:
            if arg: chrome_options.add_argument(arg)
        self.driver = webdriver.Chrome(chromedriver['path'], chrome_options=chrome_options)
        self.url = ""

    def get(self, url):
        """
        gets a page by a url
        """
        self.url = url
        self.driver.get(url)
        time.sleep(2)

    def id_text(self, id):
        """
        returns the text of an element found by id
        """
        elem = self.driver.find_element_by_id(id)
        return elem.text

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()
