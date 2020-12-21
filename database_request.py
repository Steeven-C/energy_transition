import psycopg2
from psycopg2 import OperationalError
from config import *


def create_connection(db_name,db_user,db_password,db_host,db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        cursor = connection.cursor()
        print("ça marche")
    except OperationalError as e: 
        print(f"tu es un connard ça ne marche pas '{e}'")
    return connection


def request_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id,name FROM countries;")
            request_countries = cursor.fetchall()
            cursor.execute("SELECT id,name FROM flows;")
            request_flows = cursor.fetchall()
            cursor.execute("SELECT id,name FROM products")
            request_products = cursor.fetchall()
        return request_countries, request_flows, request_products


def insert_quantities(product_id, country_id, flow_id, year, value):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO quantities(product_id, country_id, flow_id, year, value) VALUES(%s, %s, %s, %s, %s);",(product_id, country_id, flow_id, year, value))
            

connection = create_connection(name, user, password, host, port)

ids_and_countries = request_tables()
