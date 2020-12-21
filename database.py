import psycopg2
from config import user, password, host, port, name
from psycopg2 import OperationalError

""" creating connection between AWS database and our script"""


def create_conection(db_user, db_password, db_host, db_port, db_name):
    try:
        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            database=db_name)
        print("Successful connexion")
        cursor = connection.cursor()
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except OperationalError as error:
        print(f"Error while connecting to PostgreSQ {error}")

    return connection


def create_products():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(""" CREATE TABLE IF NOT EXISTS products(
            ID SERIAL PRIMARY KEY,
            NAME TEXT);
            """)


def create_flows():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(""" CREATE TABLE IF NOT EXISTS flows(
            id SERIAL PRIMARY KEY,
            name TEXT);
            """)


def create_countries():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(""" CREATE TABLE IF NOT EXISTS countries(
            id SERIAL PRIMARY KEY,
            name TEXT,
            latitude TEXT,
            longitude TEXT);
            """)


def create_quantities():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(""" CREATE TABLE IF NOT EXISTS quantities(
            id SERIAL PRIMARY KEY,
            year INT,
            value INT,
            product_id INT REFERENCES products(id),
            country_id INT REFERENCES countries(id),
            flow_id INT REFERENCES flows(id));
            """)


connection = create_conection(user, password, host, port, name)


create_products()
create_flows()
create_countries()
create_quantities()


