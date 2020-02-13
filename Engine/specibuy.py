import requests
import json


def availabilityCheck():
    r = requests.get('https://burnrubbersneakers.com/collections/sale/products.json')
    products = json.loads((r.text))['products']

    for product in products:

        product_name = product['title']

        if product_name == 'Born x Raised Stack Strap Back Hat (Green)':
            product_url = 'https://burnrubbersneakers.com/collections/sale/products/' + \
                product['handle']
            # print(product_url)
            return product_url

    return False