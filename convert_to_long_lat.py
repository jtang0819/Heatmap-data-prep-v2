import time
from googlemaps import Client as GoogleMaps
import pandas as pd
from credentials import api_key

def transform():
    gmaps = GoogleMaps(api_key)
    addresses = pd.read_csv("addresses.csv")
    addresses['long'] = ""
    addresses['lat'] = ""
    for x in range(len(addresses)):
        try:
            time.sleep(1)  # to add delay in case of large DFs
            geocode_result = gmaps.geocode(addresses['Address'][x])
            addresses['lat'][x] = geocode_result[0]['geometry']['location']['lat']
            addresses['long'][x] = geocode_result[0]['geometry']['location']['lng']
            print(addresses['lat'][x], addresses['long'][x])
        except IndexError:
            print("Address was wrong...")
        except Exception as e:
            print("Unexpected error occurred.", e)
    # addresses.head()
    addresses.to_csv('heatmap_ready.csv')
    return print(addresses.head())
