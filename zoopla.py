import json
import requests

api = 'http://api.zoopla.co.uk/api/v1/property_listings.json?listing_id=57411209&api_key=vkpf8r3nccsy4u5rpuvhpa4g'


api = 'http://api.zoopla.co.uk/api/v1/property_listings.json?listing_id=55644362&api_key=vkpf8r3nccsy4u5rpuvhpa4g'


r = requests.get(api).content
property_json = json.loads(r)['listing'][0]

property_details = {
    "address": property_json['displayable_address'],
    "postcode": property_json['outcode'],
    "countryCode": property_json['country_code'],
    "transactionType": property_json['listing_status'],
    "added": property_json['first_published_date'],
    "beds": property_json['num_bedrooms'],
    "baths": property_json['num_bathrooms'],
    "latitude": property_json['latitude'],
    "longitude": property_json['longitude'],
    "price": property_json['price'],
    "propertyId": property_json['listing_id'],
    "propertyType": property_json['property_type'],
    "agent_name": property_json['agent_name'],
    "price_changes": len(property_json['price_change'])-1,
    "original_price": property_json['price_change'][0]['price']
}

with open('property_details_zoopla.json', 'w') as f:
    json.dump(property_details, f)