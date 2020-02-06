
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options


import re
import time


class AmazonBot(object):
    def __init__(self, items):
        self.amazon_url = "https://www.amazon.ca/"
        self.items = items
        self.profile = webdriver.FirefoxProfile()
        self.options = Options()
        # self.options.headless = True
        self.driver = webdriver.Firefox(firefox_profile=self.profile,
                                        options=self.options)

        self.driver.get(self.amazon_url)

    def search_items(self):
        urls = []
        prices = []
        names = []
        for item in self.items:
            print(f'**Searching for {item}.**')
            print()

            self.driver.get(self.amazon_url)

            search_ip = self.driver.find_element_by_id('twotabsearchtextbox')
            search_ip.send_keys(item)

            time.sleep(1)

            search_button = self.driver.find_element_by_xpath(
                '/html/body/div/header/div/div[1]/div[3]/div/form/div[2]/div/input')
            search_button.click()

            time.sleep(1)
            best_value = self.driver.find_element_by_xpath('//div[@data-index="2"]')
            asin = best_value.get_attribute('data-asin')
            product_url = 'https://www.amazon.ca/dp/' + asin

            price = self.get_product_price(product_url)
            name = self.get_product_name(product_url)

            urls.append(product_url)
            prices.append(price)
            names.append(name)

            print(name)
            print(price)
            print(product_url)
            print()

            time.sleep(2)
        return prices, urls, names

        self.driver.quit()

    def get_product_price(self, url):
        self.driver.get(url)
        try:
            price = self.driver.find_element_by_id('priceblock_ourprice').text
        except:
            pass

        try:
            price = self.driver.find_element_by_id('priceblock_dealprice').text
        except:
            pass

        if price is None:
            price = 'Not available'
        else:
            price = re.compile(r'[^\d.]+').sub('', price)
        return price

    def get_product_name(self, url):
        self.driver.get(url)
        try:
            product_name = self.driver.find_element_by_id('productTitle').text
        except:
            pass

        if product_name is None:
            product_name = 'Not available'
        return product_name
