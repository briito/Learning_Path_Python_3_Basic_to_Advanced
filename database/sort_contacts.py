from bd import bd_connection

sql = 'SELECT nome, id FROM contatos ORDER BY nome DESC'

with bd_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(sql)

    print('\n'.join(str(registro) for registro in cursor))
