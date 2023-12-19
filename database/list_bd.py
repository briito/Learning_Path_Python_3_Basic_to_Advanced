import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    port=3306,
)

cursor = connection.cursor()
cursor.execute('SHOW DATABASES')


for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
