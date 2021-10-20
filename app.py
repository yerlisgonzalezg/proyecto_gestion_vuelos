import functools
from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
from flask import session
from flask import g

import os

from wtforms import form
from utils import isEmailValid, isPasswordValid, comprobarContraseñas, isEmailLoginValid, isPasswordLoginValid
from forms import Formulario_Usuario
from db import get_db, close_db


app = Flask(__name__)
app.secret_key = os.urandom(24)

def login_required(view):
    @functools.wraps( view ) # toma una función utilizada en un decorador y añadir la funcionalidad de copiar el nombre de la función.
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect( url_for( 'login' ) )
        return view( **kwargs )
    return wrapped_view

@app.route('/')
def index():
    
    return render_template("index.html")


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    try:
        if request.method == 'POST':

            nombre = request.form['nombre']
            email = request.form['email']
            password = request.form['password']
            confirmpassword = request.form['confirmpassword']

            error = None
            db = get_db()

            if not isEmailValid(email):
                error = "Correo invalido"
                flash(error)
            if not isPasswordValid(password):
                error = "La contraseña debe contener al menos una minúscula, una mayúscula, un caracter especial, un número y 8 caracteres"
                flash(error)

            if not comprobarContraseñas(password, confirmpassword):
                error = "Las contraseñas no coinciden"
                flash(error)

            user_email = db.execute(
                'SELECT * FROM Usuarios WHERE correo = ?',
                (email,)
            ).fetchone()
            if user_email is not None:
                error = "Correo ingresado ya existe."
                flash(error)

            if error is not None:
                return render_template("registro.html")
            else:
                db.execute(
                    'INSERT INTO Usuarios (nombre,correo,contrasena) VALUES (?,?,?) ',
                    (nombre, email, password)
                )
                db.commit()

                return redirect(url_for('login'))

        return render_template("registro.html")
    except:
        flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
        return render_template("registro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form= Formulario_Usuario()
    try:
        if request.method == 'POST':

            email = request.form['email']
            password = request.form['password']

            error = None
            db = get_db()

            if not isEmailLoginValid(email):
                error = "Correo invalido"
                flash(error)
            if not isPasswordLoginValid(password):
                error = "La contraseña debe contener al menos una minúscula, una mayúscula, un caracter especial, un número y 8 caracteres"
                flash(error)

            if error is not None:
                return render_template("login.html")

            else:
                user = db.execute(
                    'SELECT * FROM Usuarios WHERE correo = ? AND contrasena = ?',
                    (email, password)
                ).fetchone()
                if user is None:
                    error = "Correo y/o contraseña no son correctos."
                    flash(error)
                    return render_template("login.html")
                else:
                    session.clear()
                    session['idusuario']=user[0]

                    return redirect('dashboard')

        return render_template("login.html")
    except:
        flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
        return render_template("login.html")

    
#before request
@app.before_request
def cargar_usuario_registrado():
    id_usuario= session.get('idusuarios')
    if id_usuario is None:
        g.user=None
    else:
        g.user = get_db().execute(
                    'SELECT * FROM Usuarios WHERE idusuario = ?',
                    (id_usuario,)
                ).fetchone()

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        return render_template("dashboard.html")
    return render_template("dashboard.html")
@app.route('/logout')
def logout():
    session.clear()
    return redirect('index')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
