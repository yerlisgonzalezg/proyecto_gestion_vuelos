from flask import Flask
from flask import render_template
from flask import request, flash, redirect, url_for
import os
from utils.db import get_db, close_db
from utils.forms import*
from utils.utils import isEmailValid, isPasswordValid, comprobarContraseñas, isEmailLoginValid, isPasswordLoginValid
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, g
import functools
from repository.data_repository import*


app = Flask(__name__)
app.secret_key = os.urandom(24)


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return view(**kwargs)
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

            if not isEmailValid(email):
                error = "Correo invalido"
                flash(error)
            if not isPasswordValid(password):
                error = "La contraseña debe contener al menos una minúscula, una mayúscula, un caracter especial, un número y 8 caracteres"
                flash(error)

            if not comprobarContraseñas(password, confirmpassword):
                error = "Las contraseñas no coinciden"
                flash(error)

            user_email = consultar_usuario_reg(email,)
            if user_email is not None:
                error = "Correo ingresado ya existe."
                flash(error)

            if error is not None:
                return render_template("registro.html")
            else:
                password_cifrado = generate_password_hash(password)
                guardar_usuarios_reg(nombre, email, password_cifrado)

                return redirect(url_for('login'))

        rol_user = session.get('rol')
        if 'id_user' in session and rol_user == 'adm':
            return redirect(url_for('dashboard'))
        if 'id_user' in session and rol_user == 'user':
            return redirect(url_for('inicio_usuario'))
        if 'id_user' in session and rol_user == 'pilot':
            return redirect(url_for('inicio_usuario'))
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
                user = consultar_usuarios(email,)

                if user is None:
                    error = "Correo y/o contraseña no existe."
                    flash(error)
                    return render_template("login.html")
                else:
                    usuario_valido = check_password_hash(user[3], password)
                    if not usuario_valido:
                        error = "Usuario y/o contraseña no son correctos."
                        flash(error)
                        return render_template("login.html")
                    else:
                        session.clear()
                        session['id_user'] = user[0]
                        session['rol'] = user[4]
                        rol_usuario = session.get('rol')
                        if rol_usuario == 'adm':
                            return redirect(url_for('dashboard'))
                        return redirect(url_for('inicio_usuario'))

            return redirect(url_for('index'))

        rol = session.get('rol')
        if 'id_user' in session and rol == 'adm':
            return redirect(url_for('dashboard'))
        if 'id_user' in session and rol == 'user':
            return redirect(url_for('inicio_usuario'))
        if 'id_user' in session and rol == 'pilot':
            return redirect(url_for('inicio_usuario'))

        return render_template("login.html")
    except:
        flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
        return render_template("login.html")


@app.before_request
def cargar_usuario_registrado():
    print("Entró en before_request.")
    id_usuario = session.get('id_user')
    if id_usuario is None:
        g.user = None
    else:
        g.user = consultar_usuario_g(id_usuario)
    print('g.user:', g.user)


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    vuelos_llegada = consultar_vuelos_llegada()
    vuelos_salida = consultar_vuelos_salidas()

    rol_usuario = session.get('rol')
    if rol_usuario == 'adm':
        return render_template('dashboard.html', vuelos_llegada=vuelos_llegada, vuelos_salida=vuelos_salida)
    else:
        return redirect(url_for('acceso_denegado'))


@app.route('/crear_usuario', methods=['GET', 'POST'])
@login_required
def crear_usuario():

    rol_usuario = session.get('rol')
    if rol_usuario == 'adm':
        try:
            if request.method == 'POST':

                nombre = request.form['nombre']
                email = request.form['email']
                password = request.form['password']
                rol = "pilot"

                error = None
                db = get_db()

                if not isEmailValid(email):
                    error = "Correo invalido"
                    flash(error)
                if not isPasswordValid(password):
                    error = "La contraseña debe contener al menos una minúscula, una mayúscula, un caracter especial, un número y 8 caracteres"
                    flash(error)

                user_email = consultar_usuarios(email,)
                if user_email is not None:
                    error = "Correo ingresado ya existe."
                    flash(error)

                if error is not None:
                    return render_template("crear_usuario.html")
                else:
                    password_cifrado = generate_password_hash(password)

                    guardar_usuarios_pilot(
                        nombre, email, password_cifrado, rol)

                    return redirect(url_for('login'))

            return render_template("crear_usuario.html")
        except:
            flash("¡Ups! Ha ocurrido un error, intentelo de nuevo.")
            return render_template("crear_usuario.html")
    else:
        return redirect(url_for('acceso_denegado'))


@app.route('/buscar_vuelos', methods=['GET', 'POST'])
@login_required
def buscar_vuelos():
    return render_template('buscar_vuelos.html')


@app.route('/buscar_vuelos_ida_vuelta', methods=['GET', 'POST'])
@login_required
def buscar_vuelos_ida_vuelta():

    if request.method == 'POST':
        origen = request.form['origen']
        destino = request.form['destino']
        ida = request.form['ida']
        regreso = request.form['regreso']
        pasajero = request.form['pasajero']

        if not origen:
            flash('El campo de Origen no debe estar vacío')
        if not destino:
            flash('El campo de Destino no debe estar vacío')
        if not ida:
            flash('El campo de Fecha de ida no debe estar vacío')
        if not regreso:
            flash('El campo de Fecha de regreso no debe estar vacío')
        if not pasajero:
            flash('El campo de No de pasajeros no debe estar vacío')
        if origen and destino and ida and regreso and pasajero:

            vuelos = consultar_vuelos(origen, destino, ida, regreso)

            return render_template("buscar_vuelos_ida_vuelta.html", vuelos=vuelos)

    return render_template("buscar_vuelos_ida_vuelta.html")


@app.route('/buscar_vuelos_ida', methods=['GET', 'POST'])
@login_required
def buscar_vuelos_ida():

    if request.method == 'POST':
        origen = request.form['origen']
        destino = request.form['destino']
        ida = request.form['ida']
        pasajero = request.form['pasajero']

        if not origen:
            flash('El campo de Origen no debe estar vacío')
        if not destino:
            flash('El campo de Destino no debe estar vacío')
        if not ida:
            flash('El campo de Fecha de ida no debe estar vacío')
        if not pasajero:
            flash('El campo de No de pasajeros no debe estar vacío')
        if origen and destino and ida and pasajero:
            vuelos = consultar_vuelos_ida(origen, destino, ida)
            return render_template("buscar_vuelos_ida.html", vuelos=vuelos)

    return render_template("buscar_vuelos_ida.html")


@app.route('/agregar_vuelo', methods=['GET', 'POST'])
@login_required
def agregar_vuelos():
    rol_usuario = session.get('rol')
    if rol_usuario == 'adm':
        return render_template('agregar_vuelo.html')
    else:
        return redirect(url_for('acceso_denegado'))


@app.route('/eliminar_vuelos', methods=['GET', 'POST'])
@login_required
def eliminar_vuelos():
    rol_usuario = session.get('rol')
    if rol_usuario == 'adm':
        return render_template('eliminar_vuelos.html')
    else:
        return redirect(url_for('acceso_denegado'))


@app.route('/modificar_vuelos', methods=['GET', 'POST'])
@login_required
def modificar_vuelos():
    rol_usuario = session.get('rol')
    if rol_usuario == 'adm':
        return render_template('modificar_vuelos.html')
    else:
        return redirect(url_for('acceso_denegado'))


@app.route('/reservas', methods=['GET', 'POST'])
@login_required
def reservas():
    return render_template('reservas.html')


@app.route('/calificar_vuelo', methods=['GET', 'POST'])
@login_required
def calificar_vuelo():
    return render_template('calificar_vuelo.html')


@app.route('/comentarios', methods=['GET', 'POST'])
@login_required
def comentarios():
    return render_template('comentarios.html')


@app.route('/inicio_usuario')
@login_required
def inicio_usuario():
    return render_template('inicio_usuario.html')


@app.route('/acceso_denegado')
def acceso_denegado():
    return render_template('acceso_denegado.html')


@app.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
