import pandas as pd
import time
from geopy.geocoders import Nominatim
from database_request import ids_and_countries


# Lecture du fichier excel avec limitation du nombre de ligne
df = pd.read_excel(
    "data/WorldEnergyBalancesHighlights_final.xlsx",
    sheet_name="TimeSeries_1971-2019",
    skiprows=1,
    usecols="A:BB",
    engine="openpyxl",
)
df = df[:6048]


unique_products = df.Product.unique()
products = pd.DataFrame({"name": unique_products})

unique_flows = df.Flow.unique()
flows = pd.DataFrame({"name": unique_flows})


# partie clement
latitude = []
longitude = []

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
            address = name
            geolocator = Nominatim(user_agent="Your_Name")
            location = geolocator.geocode(address)
            lat.append((location.latitude))
            lon.append((location.longitude))
        except:
            lat.append(word)
            lon.append(word)

df2['lat'] = pd.DataFrame(lat)
df2['lon'] = pd.DataFrame(lon)

df2 = df2.rename(columns={'Country': 'name', 'lat': 'latitude', 'lon': 'longitude'})

# partie steeven

df_final = df.copy()
df_final
df_final = df_final.drop(["NoCountry", "NoProduct", "NoFlow"], axis=1)
df_final = df_final.replace("..", 0)
df_final = df_final.replace("c", 0)


df_final = df_final.transpose()
dict_final = df_final.to_dict()

data = []
for key in dict_final.keys():
    dictionnary = dict_final[key]
    data.append(dictionnary)


total_lines = []


def create_total_lines(empty_list=list):
    for dictionnary in data:
        key = dictionnary.keys()
        list_year = list(key)[3:]
        for year in list_year:
            lines = {
                "country": dictionnary["Country"],
                "product": dictionnary["Product"],
                "flow": dictionnary["Flow"],
                "year": year,
                "value": dictionnary[year]
            }
            # lines["country"]= dictionnary["Country"]
            # lines["product"]= dictionnary["Product"]
            # lines["Flow"]= dictionnary["Flow"]
            # lines["year"] = year
            # lines["value"] = dictionnary[year]
            # print(lines)
            empty_list.append(lines)
    return empty_list


create_total_lines(total_lines)


for element in total_lines:
    for line in ids_and_countries[0]:
        if element["country"] == line[1]:
            element["country_id"] = line[0]
    for line in ids_and_countries[1]:
        if element["flow"] == line[1]:
            element["flow_id"] = line[0]
    for line in ids_and_countries[2]:
        if element["product"] == line[1]:
            element["product_id"] = line[0]

print(total_lines)