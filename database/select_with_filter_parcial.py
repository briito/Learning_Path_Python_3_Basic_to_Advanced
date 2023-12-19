from bd import bd_connection

sql = "SELECT * FROM contatos WHERE nome like 'Lu%'"

with bd_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
