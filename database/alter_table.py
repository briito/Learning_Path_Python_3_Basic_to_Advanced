from mysql.connector.errors import ProgrammingError
from bd import bd_connection

sql = 'ALTER TABLE contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
