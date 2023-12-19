from bd import bd_connection

sql = "SELECT * FROM contatos WHERE tel = '98765-4321'"

with bd_connection() as conn:
    cursor = conn.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
