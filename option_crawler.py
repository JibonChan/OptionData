import requests
import json
from datetime import datetime


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
        while data.status_code != 200:
            data = requests.get(url, headers=headers)

    return data.text


def main():
    timestamp = datetime.now()
    data = json.loads(fetch())
    data["timeStamp"] = str(timestamp)
    path = '/home/jibon/OptionData/'
    filename = path + str(timestamp) + ".json"

    with open(filename, "w") as f:
        f.write(json.dumps(data, ensure_ascii=False))

main()