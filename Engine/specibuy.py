import requests
import json
import time
import userCreds
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys


def availabilityCheck():
    r = requests.get('https://burnrubbersneakers.com/collections/sale/products.json')
    products = json.loads((r.text))['products']
    for product in products:
        product_name = product['title']
        if product_name == 'Born x Raised Stack Strap Back Hat (Green)':
            product_url = 'https://burnrubbersneakers.com/collections/sale/products/' + \
                product['handle']
            # print(product_url)
            print('Product Found!')
            return product_url

    return False


def buyProduct(url):
    driver = webdriver.Firefox()
    driver.get(str(url))
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[2]/div/div/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@value="Add to Cart"]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="cartToggle"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/header/div/div[1]/div/div[4]/div/div/div[2]/div[2]/button').click()
    time.sleep(3)
    fillCredentials(driver)


def fillCredentials(driver):
    driver.find_element_by_xpath(
        '//*[@id="checkout_email"]').send_keys(userCreds.email)
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_first_name"]').send_keys(userCreds.first_name)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_last_name"]').send_keys(userCreds.last_name)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_address1"]').send_keys(userCreds.address)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_city"]').send_keys(userCreds.city)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_zip"]').send_keys(userCreds.postal_code)
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_phone"]').send_keys(userCreds.phone + 'u\ue007')


my_url = availabilityCheck()
if my_url is False:
    print('Not Available')
else:
    buyProduct(my_url)