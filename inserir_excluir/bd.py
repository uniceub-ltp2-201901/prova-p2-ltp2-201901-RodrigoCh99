
def get_contatos(cursor):
    # Executar o SQL
    cursor.execute(f'SELECT idcontatos, nome, email From contatos;')

    # Recuperando o retorno do Banco de Dados
    contatos = cursor.fetchall()

    # fechar o cursor
    cursor.close()

    # print
    print(contatos[0:])

    # Retornan os contatos
    return contatos


def set_contato(cursor, conn, nome, email):
    # Executar o SQL
    cursor.execute(f'INSERT INTO contatos (nome, email) VALUES("{nome}","{email}")')

    # confirmar inserção:
    conn.commit()

def del_contato(cursor, conn, id):
    # Executar o SQL
    cursor.execute(f'DELETE from contatos WHERE idcontatos = { id }') # como o id não é númerico ele não necessita de aspas duplas

    # confirmar inserção:
    conn.commit()


def get_info(cursor, id):
    # Executar o SQL
    cursor.execute(f'SELECT * FROM contatos WHERE idcontatos = { id }')

    info = cursor.fetchone()
    print(info)

    return info


def alter_contato(conn, cursor, new_nome, new_email, id):
    # Executar o SQL
    cursor.execute(f"""UPDATE contatos SET nome="{ new_nome }", email= "{ new_email }" WHERE idcontatos = { id }""")

    # confirmar inserção:
    conn.commit()
