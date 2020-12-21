import pandas as pd
import openpyxl
from database_request import ids_and_countries, insert_quantities
df = pd.read_excel('WorldEnergyBalancesHighlights_final.xlsx', sheet_name = 'TimeSeries_1971-2019',skiprows = 1, usecols='A:BB', engine='openpyxl')

df= df[:6048]

df_final = df.copy()
df_final
df_final = df_final.drop(["NoCountry","NoProduct","NoFlow"],axis= 1)
df_final = df_final.replace("..", 0)

df_final = df_final.transpose()
dict_final = df_final.to_dict()
dict_final


data = []
for key in dict_final.keys():
    dictionnary = dict_final[key]
    data.append(dictionnary)

# print(data)


# print(len(data))
total_lines = []

def create_total_lines(empty_list= list):
    for dictionnary in data:  
    #     print(dictionnary.keys())
        key = dictionnary.keys()
        list_year = list(key)[3:]
        for year in list_year : 
            lines = {
                "country":dictionnary["Country"],
                "product": dictionnary["Product"],
                "flow": dictionnary["Flow"],
                "year": year,
                "value":dictionnary[year],
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
# print(total_lines)

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
        

        # print(line)


# print(total_lines)

for element in total_lines:
    insert_quantities(element["product_id"], element["country_id"], element["flow_id"], element["year"], element["value"])
    print(element["product_id"], '|', element["country_id"], '|', element["flow_id"], '|', element["year"], '|', element["value"])