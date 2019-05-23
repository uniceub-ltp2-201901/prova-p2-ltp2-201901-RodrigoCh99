from flask import Flask, request, render_template, url_for, redirect
from flaskext.mysql import MySQL
from bd import *

# Instanciando a app Flask
app = Flask(__name__)

# Instanciando o objeto mysql
mysql = MySQL()

# Ligar o MySQL ao Flask
mysql.init_app(app)

# configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'contatos'



# Rota para /
@app.route('/')
def principal():
    return render_template('index.html')

# rota para /listar
@app.route('/listar')
def listar():

    # obtendo a conexão com BD
    conn = mysql.connect()

    # obtendo o cursor para acessar o banco de daods
    cursor = mysql.get_db().cursor()

    return render_template('lista.html', contatos=get_contatos(cursor))

# rota para /inserir -> formulario
@app.route('/inserir')
def inserir():
    return render_template('inserir.html')


@app.route('/inserido', methods=['POST'])
def inserido():

    if request.method == 'POST':
        # variaveis vindas do form
        nome = request.form.get('nome')
        e_mail = request.form.get('email')

        # obtendo a conexão com BD
        conn = mysql.connect()

        # obtendo o cursor para acessar o banco de daods
        cursor = conn.cursor()

        # função para inserir contato
        set_contato(cursor, conn, nome, e_mail)

        # Fechar o cursor
        cursor.close()

        # Fechar a conexão
        conn.close()

        # retornando a lista nova
        return redirect(url_for('listar'))


    else:

        # volta o usuario para o formulario
        return inserir

@app.route('/deletar/<id>')
def deletar_linha(id):

    # obtendo a conexão com BD
    conn = mysql.connect()

    # obtendo o cursor para acessar o banco de daods
    cursor = conn.cursor()

    # função para deletar do BD
    del_contato(cursor, conn, id)

    # Fechar o cursor
    cursor.close()

    # Fechar a conexão
    conn.close()

    # retornando a lista nova
    return redirect(url_for('listar'))

@app.route('/form_alteracao/<id>')
def formulario_alteracao(id):

    # obtendo a conexão com BD
    conn = mysql.connect()

    # obtendo o cursor para acessar o banco de daods
    cursor = conn.cursor()

    informacoes = get_info(cursor, id)

    return render_template('formulario_de_altercao.html', info=informacoes)

@app.route('/alteracao', methods=['GET','POST'])
def alteracao():

    # obtendo a conexão com BD
    conn = mysql.connect()

    # obtendo o cursor para acessar o banco de daods
    cursor = conn.cursor()

    # variaveis vindas do form
    novo_nome = request.form.get('novo_nome')
    novo_e_mail = request.form.get('novo_email')
    id = request.form.get('id')

    print(novo_nome)
    print(novo_e_mail)
    print(id)

    alter_contato(conn, cursor, novo_nome, novo_e_mail, id)

    return redirect(url_for('listar'))


# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)
