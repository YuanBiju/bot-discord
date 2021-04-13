import requests
import json 

def crypto_output(crypto_name):
    response = requests.get("https://api.wazirx.com/api/v2/market-status")
    json_response = response.json()
    markets = json_response["markets"]
    l = len(markets)
    market = markets[0]
    for i in range(0,l):
        if (markets[i]["quoteMarket"] == "inr") and (markets[i]["baseMarket"] == crypto_name):
            market=markets[i]

    return market