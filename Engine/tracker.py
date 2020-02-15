
from selenium import webdriver
from notifier import SendMail
from selenium.webdriver.firefox.options import Options

import time
import re

def getPrice(driver):
    title = driver.find_element_by_xpath(
        '//span[@id="productTitle"]').text
    try:
        original_price = driver.find_element_by_xpath(
        '//span[@id="priceblock_ourprice"]').text
    except:
        pass
    try:
        original_price = driver.find_element_by_xpath(
            '//span[@id="priceblock_dealprice"]').text
    except:
        pass
    formatted_original_price = re.compile(r'[^\d.]+').sub('', original_price)
    print(original_price)
    print(formatted_original_price)
    return title, original_price, float(formatted_original_price)


def getUpdatedPrice(driver):
    try:
        updated_price = driver.find_element_by_xpath(
            '//span[@id="priceblock_ourprice"]').text
    except:
        pass
    try:
        updated_price = driver.find_element_by_xpath(
            '//span[@id="priceblock_dealprice"]').text
    except:
        pass

    formatted_updated_price = re.compile(r'[^\d.]+').sub('', updated_price)
    return updated_price, float(formatted_updated_price)

def trackEvent(textboxValue):
    url = textboxValue
    options = Options()
    #options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    info = [0, 0, 0]
    name, original_price, converted_original_price = getPrice(driver)
    info[0] = name
    info[1] = original_price
    while(True):            # repeatedly checks for price changes
        updated_price, converted_updated_price = getUpdatedPrice(driver)
        info[2] = updated_price
        if(converted_updated_price < converted_original_price):
            print(info)
            print('Price decreased! \n Sending email....')
            SendMail(2, info)
        time.sleep(43200)
    driver.quit()
