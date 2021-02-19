
import json
import re

import requests

url = 'https://www.rightmove.co.uk/properties/88317910#/'
r = requests.get(url)
page = r.content.decode('utf-8')

page_str = page.split('window.PAGE_MODEL = ')[-1]

property_string = re.search('({.+})', page_str).group(0)
property_json = json.loads(property_string)

property_details = {
    "address": property_json['propertyData']['address']['displayAddress'],
    "postcode": property_json['analyticsInfo']['analyticsProperty']['postcode'],
    "countryCode": property_json['propertyData']['address']['countryCode'],
    "tenureType": property_json['propertyData']['tenure']['tenureType'],
    "yearsRemainingOnLease": property_json['propertyData']['tenure']['yearsRemainingOnLease'],
    "transactionType": property_json['propertyData']['transactionType'],
    "added": property_json['analyticsInfo']['analyticsProperty']['added'],
    "beds": property_json['analyticsInfo']['analyticsProperty']['beds'],
    "currency": property_json['analyticsInfo']['analyticsProperty']['currency'],
    "latitude": property_json['analyticsInfo']['analyticsProperty']['latitude'],
    "longitude": property_json['analyticsInfo']['analyticsProperty']['longitude'],
    "ownership": property_json['analyticsInfo']['analyticsProperty']['ownership'],
    "price": property_json['analyticsInfo']['analyticsProperty']['price'],
    "priceQualifier": property_json['analyticsInfo']['analyticsProperty']['priceQualifier'],
    "propertyId": property_json['analyticsInfo']['analyticsProperty']['propertyId'],
    "propertySubType": property_json['analyticsInfo']['analyticsProperty']['propertySubType'],
    "propertyType": property_json['analyticsInfo']['analyticsProperty']['propertyType']
}

with open('property_details_rightmove.json', 'w') as f:
    json.dump(property_details, f)
