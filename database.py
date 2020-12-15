import psycopg2
from code import user, password, host, port, name
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
    except OperationalError as error:
        print(f"The error is {error}")
    return connection


connection = create_conection(user, password, host, port, name)
