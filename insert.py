from clean_data import products, flows, df2, total_lines
from sqlalchemy import create_engine
from database_request import insert_quantities
from config import *


# Connection à la db
uri = f'postgres://{user}:{password}@{host}:{port}/{name}'
engine = create_engine(uri)
# Pour mettre toute les donnée du df dans la db
products.to_sql(name="products", con=engine, if_exists="append", index=False)
flows.to_sql(name="flows", con=engine, if_exists="append", index=False)


# partie clement
df2.to_sql('countries', con=engine, if_exists='append', index=False)
engine.execute("SELECT * FROM countries").fetchall()


# partie steeven
for element in total_lines:
    insert_quantities(element["product_id"], element["country_id"], element["flow_id"], element["year"], element["value"])
    print(element["product_id"], '|', element["country_id"], '|', element["flow_id"], '|', element["year"], '|', element["value"])