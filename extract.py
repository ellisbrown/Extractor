# extract.py
# ----------
# Ellis Brown

"""
Uses selenium and chromium webdriver to extract page information from javascript loaded sites
"""

import time
from selenium import webdriver

CHROME_DRIVER_PATH = '/home/brownel3/workspace/chromedriver'

class Extract(object):

    def __init__(self, url):
        """
        initializes a chromedriver instance and  a base url
        gets the url and waits for the js on the page to load
        """
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
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