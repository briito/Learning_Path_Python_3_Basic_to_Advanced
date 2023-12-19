from mysql.connector.errors import ProgrammingError
from bd import bd_connection

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS emails')
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
