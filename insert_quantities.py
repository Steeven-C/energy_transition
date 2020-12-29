from clean_data import total_lines

from sqlalchemy import create_engine
from database_request import insert_quantities
from config import *


# partie steeven
for element in total_lines:
    insert_quantities(element["product_id"], element["country_id"], element["flow_id"], element["year"], element["value"])
    print(element["product_id"], '|', element["country_id"], '|', element["flow_id"], '|', element["year"], '|', element["value"])