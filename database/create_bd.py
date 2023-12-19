import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    port=3306,
)

cursor = connection.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS agenda')
