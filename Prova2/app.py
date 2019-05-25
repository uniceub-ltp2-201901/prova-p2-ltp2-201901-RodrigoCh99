# Nome: Rodrigo Pereira da Rocha
# RA: 21802562

from flask import Flask, render_template, request, redirect, url_for
from bd import *
from flaskext.mysql import MySQL

# Instanciando o objeto Flask
app = Flask(__name__)

# Instanciando o objeto mysql
mysql = MySQL()

# Ligar o MySQL ao Flask
mysql.init_app(app)

# configurando o acesso ao MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'encurtador'


@app.route('/')
def index():
    return render_template('index.html', variavel=randomic_int())



@app.route('/save_url', methods=['GET','POST'])
def update():
    original = request.form.get('longa')
    novo = request.form.get('encurtada')


    # obtendo a conexão com BD
    conn = mysql.connect()

    # obtendo o cursor para acessar o banco de daods
    cursor = conn.cursor()

    insert_into_db(original, novo, conn, cursor)


    return render_template('sucesso.html', nova_url=create_new_url(novo))


@app.route('/http://127.0.0.1:5000/<cod>', methods=['GET', 'POST'])
def url_fixer(cod):
    if request.method == "GET":
        # obtendo a conexão para acessar o BD
        conn = mysql.connect()

        # obtendo o cursor para acessar o banco de daods
        cursor = conn.cursor()


        site = get_url_with_cod(cod, cursor)


        return redirect(url_for(site))
    else:
        return render_template('index.html')








# Rodando a app
if __name__ == '__main__':
    app.run(debug=True)