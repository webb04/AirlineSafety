#!/usr/bin/env python3
import requests

API_KEY = ""


def _poll_live_pricing(session_url):
    return requests.get("{}?apikey={}".format(session_url, API_KEY))


session_response = requests.post("http://business.skyscanner.net/apiservices/pricing/v1.0/?apikey=".format(API_KEY),
                                 data={'country': 'UK',
                                       'currency': 'GBP',
                                       'locale': 'en-GB',
                                       'locationSchema': 'iata',
                                       'apikey': API_KEY,
                                       'grouppricing': 'on',
                                       'originplace': 'JFK',
                                       'destinationplace': 'LHR',
                                       'pagesize': 1,
                                       'includecarriers': '001',
                                       'outbounddate': '2017-12-17',
                                       'inbounddate': '2017-12-17'})

session_url = session_response.headers['Location']

print("Session URL from Skyscanner: {}".format(session_url))

pricing_response = _poll_live_pricing(session_url)
while pricing_response.status_code != 200:
    pricing_response = _poll_live_pricing(session_url)



# url = "https://api.private-beta-1.pusherplatform.com:443/apps/bf294293-08b7-4f18-8f61-44eefd49d19b/feeds/getting-started"
# # https://dash.pusher.com/apps/bf294293-08b7-4f18-8f61-44eefd49d19b/feeds/inspector
#
# payload = "{\"items\":" + str(pricing_response.json()['Segments'][0]) + "}"
#
# response = requests.request("POST", url, data=payload)
#
# print(response.text)




print(pricing_response.json()['Segments'])
