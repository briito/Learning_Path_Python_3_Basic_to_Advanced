from bd import bd_connection

with bd_connection() as conn:
    cursor = conn.cursor()
    cursor.execute('SHOW TABLES')

    for i, table in enumerate(cursor, start=1):
        print(f'Tabela {i}: {table[0]}')
