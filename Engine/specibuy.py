import requests
import json
import time
import csv
from notifier import SendMail
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def availabilityCheck(textboxValue):
    r = requests.get('https://burnrubbersneakers.com/collections/sale/products.json')
    products = json.loads((r.text))['products']

    for product in products:

        product_name = product['title']
        if product_name == textboxValue:
            product_url = 'https://burnrubbersneakers.com/collections/sale/products/' + \
                product['handle']
            print('Product Found!')
            return product_url

    return False


def buyProduct(url, price):
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get(str(url))
    previous_price = driver.find_element_by_xpath(
        '//span[@class="compare-price money"]').text
    current_price = driver.find_element_by_xpath(
        '//span[@class="price on-sale money"]').text
    price.append(previous_price)
    price.append(current_price)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[5]/div[1]/div[2]/div/div/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//input[@value="Add to Cart"]').click()
    time.sleep(6)
    driver.find_element_by_xpath('//*[@id="cartToggle"]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/header/div/div[1]/div/div[4]/div/div/div[2]/div[2]/button').click()
    time.sleep(2)
    fillCredentials(driver)
    time.sleep(2)
    driver.quit()


def fillCredentials(driver):
    with open('/home/hakanohi/Projects/Grabber/Engine/checkoutInfo.csv', 'rt') as creds:
        csv_reader = csv.reader(creds)
        for line in csv_reader:
            checkoutInfo = line

    driver.find_element_by_xpath(
        '//*[@id="checkout_email"]').send_keys(checkoutInfo[0])
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_first_name"]').send_keys(checkoutInfo[1])
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_last_name"]').send_keys(checkoutInfo[2])
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_address1"]').send_keys(checkoutInfo[3])
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_city"]').send_keys(checkoutInfo[4])
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_zip"]').send_keys(checkoutInfo[5])
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="checkout_shipping_address_phone"]').send_keys(checkoutInfo[6] + 'u\ue007')

def buyEvent(textboxValue):
    price = []
    my_url = availabilityCheck(textboxValue)
    if my_url is False:
        print('Not Available')
    else:
        try:
            buyProduct(my_url, price)
        except:
            print('The product cannot be purchased onine!')
