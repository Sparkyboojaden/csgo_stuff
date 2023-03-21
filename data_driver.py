import pandas as pd
import requests
from database import update_table
import pyotp
from config import bitskins_secret, bitskins_api_key
import json

def skinport():
    params={
        "app_id": 730,
        "currency": "USD",
        "tradable": 0
    }
    response = requests.get("https://api.skinport.com/v1/items", params=params).json()

    df = pd.DataFrame.from_dict(response)
    update_table(df,"skinport")

def bitskins():
    my_token = pyotp.TOTP(bitskins_secret)

    code = my_token.now()
    app_id = 730 

    url = f"https://bitskins.com/api/v1/get_price_data_for_items_on_sale/?api_key={bitskins_api_key}&code={code}&app_id={app_id}"

    response = requests.get(url).json()
    response = response["data"]["items"]
    df = pd.json_normalize(response, sep="_")
    
    update_table(df,"bitskins")

def waxpeer():
    url = "https://api.waxpeer.com/v1/prices"
    params = {  
        "game": "csgo",
        "minified": "1",
        "highest_offer": "0",
        "single": "0"
    }
    headers = {"Accept": "application/json"}

    response = requests.get(url, params=params, headers=headers).json()
    response = response["items"]
    df = pd.DataFrame(response)
    df["min"] = df["min"]/1000
    update_table(df,"waxpeer")

waxpeer()

