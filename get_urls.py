
import requests
import os
import json

def make_url_hit():
    # urls="https://hermes.goibibo.com/hotels/v2/search/data/v3/4213513766539949483/20161027/20161028/1-1_0?s=popularity&cur=INR&f={}&pid=1"
    # page = urllib.urlopen(urls).read()
    # print(page)

    hotelJson = requests.get(
                "https://hermes.goibibo.com/hotels/v2/search/data/v3/4213513766539949483/20161027/20161028/1-1_0?s=popularity&cur=INR&f={}&pid=1").json()
    with open('myfile.json', 'w') as outfile:
        json.dump(hotelJson, outfile)
    os.system("python gen_outline.py --collection data myfile.json")
    os.system("python json2csv.py myfile.json myfile.outline.json")
    return

make_url_hit()
