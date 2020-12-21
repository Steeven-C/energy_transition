import pandas as pd
import time
from geopy.geocoders import Nominatim
df = pd.read_excel('data_energy.xlsx', sheet_name='TimeSeries_1971-2019', usecols='A:BB', engine='openpyxl')
df.columns = df.iloc[0]
df = df.drop([0])
df = df[:6048]


latitude=[]
longitude=[]

new = df[['Country']]
df2 = new.drop_duplicates(subset=['Country'])
df2 = df2.reset_index()
df2 = df2.drop(columns=['index'])


lat = []
lon = []
for row in df2.itertuples(index=False):
    for name in row:
        time.sleep(0.5)
        word = "NULL"
        try:
            address=name
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(address)
            lat.append((location.latitude))
            lon.append((location.longitude))
        except:
            lat.append(word)
            lon.append(word)
        

df2['lat'] = pd.DataFrame(lat)
df2['lon'] = pd.DataFrame(lon)


df2 = df2.rename(columns = {'Country':'name', 'lat': 'latitude', 'lon': 'longitude'})




