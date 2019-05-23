from flask import Flask, render_template, request, redirect, url_for
from flaskext import MySQL

app = Flask(__name__)

mysql = MySQL()

mysql.init_app(app)

