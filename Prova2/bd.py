import random


def randomic_int():
    var = random.randint(10000, 99999)

    return var

def insert_into_db(original, novo, conn, cursor):
    # Executar o sql

    cursor.execute(f'INSERT INTO urls (url, codigo) VALUES ("{original}", "{novo}")')
    # comitando as mudanças no banco de dados
    conn.commit()

def create_new_url(codigo):
    new_url = 'http://127.0.0.1:5000/' + str(codigo)
    print(new_url)
    return new_url

def get_url_with_cod(cod, cursor):
    cursor.execute(f'select url from urls where codigo = "{str(cod)}"; ')
    print(request.url)
    site = cursor.fetchone()
    print(site)

    return site