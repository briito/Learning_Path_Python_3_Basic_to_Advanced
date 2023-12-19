from bd import bd_connection

with bd_connection() as conn:
    if conn.is_connected():
        print('Conectado!')

print('Fim :)')