import requests
import json
from datetime import datetime
import os
import pandas as pd


def fetch():
    headers = {
        "Host": "www.nseindia.com",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "utf8"
    }
    url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
    data = requests.get(url, headers=headers)
    if data.status_code != 200:
        data = requests.get(url, headers=headers)
        count = 0
        while data.status_code != 200 and count < 5:
            count += 1
            data = requests.get(url, headers=headers)

    return data.text

def _formatData(data):
    list_of_dfs = [pd.DataFrame(d['PE'], index=[0]) for d in data['filtered']['data']]
    df1 = pd.concat(list_of_dfs)
    df1['bidType'] = 'PE'

    list_of_dfs = [pd.DataFrame(d['CE'], index=[0]) for d in data['filtered']['data']]
    df2 = pd.concat(list_of_dfs)
    df2['bidType'] = 'CE'

    df = pd.concat([df1, df2], axis=0, ignore_index=True)

def _action():
    data = json.loads(fetch())
    timestamp = datetime.now()
    data["timeStamp"] = str(timestamp)
    path = f'./{timestamp.date()}/'
    filename = path + str(timestamp.date()) + ' ' + str(timestamp.time()).replace(':', '-').split('.')[0] + ".json"

    with open(filename, "w") as f:
        f.write(json.dumps(data, ensure_ascii=False))

def main():

    ct = datetime.now()
    
    if ct.hour in range(9, 16) and ct.weekday() in range(0,5):
        if not os.path.exists(str(ct.date())):
            os.mkdir(str(ct.date())) 
        _action()
    else:
        print("Market is closed now !")

main()