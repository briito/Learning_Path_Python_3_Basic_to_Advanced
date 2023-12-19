from bd import bd_connection

sql = "SELECT * FROM contatos WHERE nome like %s"

with bd_connection() as conn:
    nome = input('Contato a localizar: ')
    args = (f'%{nome}%', )

    cursor = conn.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
