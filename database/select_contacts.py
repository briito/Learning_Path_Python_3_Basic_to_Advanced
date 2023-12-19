from mysql.connector.errors import ProgrammingError
from bd import bd_connection

sql = 'SELECT * FROM contatos'
# sql = 'SELECT * FROM contatos LIMIT % OFFSET %'
# args = (5,3)

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql) #args
        contacts = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:10s} Telefone: {contact[1]}')
