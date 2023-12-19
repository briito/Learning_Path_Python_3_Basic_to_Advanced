import mysql.connector
from contextlib import contextmanager


config = dict(
    host='localhost',
    user='root',
    password='1234',
    port=3306,
    database='agenda'
)


@contextmanager
def bd_connection():
    connection = mysql.connector.connect(**config)
    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Conexão ao MySQL fechada.")
