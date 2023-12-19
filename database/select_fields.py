from bd import bd_connection

sql = 'SELECT tel, nome FROM contatos'

with bd_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(sql)

    for contato in cursor.fetchall():
        print('\t'.join(str(campo) for campo in contato))
