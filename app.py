from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import os
from db  import consultar_vuelos_llegada,consultar_vuelos_salidas, consultar_total_operaciones, consultar_total_llegadas,consultar_total_salidas
from utils import isEmailValid, isPasswordValid, comprobarContraseñas, isEmailLoginValid, isPasswordLoginValid
from forms import Formulario_Usuario
from db import get_db, close_db
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = os.urandom(24)


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
                password_cifrado = generate_password_hash(password)
                db.execute(
                    'INSERT INTO Usuarios (nombre,correo,contrasena) VALUES (?,?,?) ',
                    (nombre, email, password_cifrado)
                )
                db.commit()

                return redirect(url_for('login'))

        return render_template("registro.html")
    except:
        flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
        return render_template("registro.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
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
                    # 'SELECT * FROM Usuarios WHERE correo = ? AND contrasena = ?',
                    'SELECT idusuarios, nombre, correo, contrasena FROM usuarios WHERE correo = ?',
                    (email,)
                ).fetchone()
                if user is None:
                    error = "Correo y/o contraseña no existe."
                    flash(error)
                    return render_template("login.html")
                else:
                    usuario_valido = check_password_hash(user[3], password)
                    if not usuario_valido:
                        error = "Usuario y/o contraseña no son correctos."
                        flash(error)
                    return redirect(url_for('dashboard'))
        return render_template("login.html")
    except:
        flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
        return render_template("login.html")

@app.route('/dashboard', methods=['GET', 'POST'])
#@login_required
def dashboard():
    vuelos_llegada=consultar_vuelos_llegada()
    vuelos_salida=consultar_vuelos_salidas()
    operaciones=consultar_total_operaciones()
    llegadas=consultar_total_llegadas()
    salidas=consultar_total_salidas()
    print("cantidad de operaciones",llegadas)
    return render_template('dashboard.html', vuelos_llegada=vuelos_llegada,vuelos_salida=vuelos_salida,operaciones=operaciones,llegadas=llegadas, salidas=salidas )




if __name__ == '__main__':
    app.run(debug=True, port=5000)
