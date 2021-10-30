from requests import request
from json import loads
import pandas as pd


def structure(d):
    places = d["places"][0]
    df = pd.DataFrame.from_dict(list(places.items()), orient="columns")
    return df


def req(z):
    url = 'https://api.zippopotam.us/us/{}'.format(z)
    r = request('GET', url)
    return loads(r.text)


#zips = ['77517', '77372', '77259', '84326']
# for z in zips:
z = input("Enter zip code: ")
data = req(z)
df = structure(data)
print(df)
