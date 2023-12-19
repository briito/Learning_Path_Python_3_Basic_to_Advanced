from mysql.connector.errors import ProgrammingError
from bd import bd_connection

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('Soldado', '98156-9203')

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('1 registro incluído, ID:', cursor.lastrowid)
