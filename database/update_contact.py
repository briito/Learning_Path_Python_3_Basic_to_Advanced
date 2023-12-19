from mysql.connector.errors import ProgrammingError
from bd import bd_connection

sql = 'UPDATE contatos SET nome = %s WHERE id = %s'
args = ('Lucas Yuri', 6)

with bd_connection() as conn:
    try:
        cursor = conn.cursor()
        cursor.execute(sql, args)
        conn.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) alterado(s).')
