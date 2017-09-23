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

pricing_response = _poll_live_pricing(session_url)
while pricing_response.status_code != 200:
    pricing_response = _poll_live_pricing(session_url)
