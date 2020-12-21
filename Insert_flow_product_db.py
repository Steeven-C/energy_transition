from create_flow_product_dataframe import products, flows
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

# Connection à la db
sql_engine = create_engine(
    f"postgresql://{identifiant}:{password}@{adresse}:{port}/postgres"
)

# Pour mettre toute les donnée du df de plans aille dans la db
products.to_sql(name="products", con=sql_engine, if_exists="append", index=False)
flows.to_sql(name="flows", con=sql_engine, if_exists="append", index=False)

