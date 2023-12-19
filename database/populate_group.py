from mysql.connector.errors import ProgrammingError
from bd import bd_connection

sql = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('Casa',),
    ('Trabalho',),
)

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, args)
        conn.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
