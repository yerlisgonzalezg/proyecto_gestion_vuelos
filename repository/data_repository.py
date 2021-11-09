from utils.db import sql_connection, close_db, get_db


def consultar_usuario_reg(email):
    db = get_db()
    cursor = db.execute('SELECT * FROM Usuarios WHERE correo = ?',
                        (email,)).fetchone()
    return cursor


def consultar_usuarios(email):
    db = get_db()
    cursor = db.execute(
        'SELECT idusuarios, nombre, correo, contrasena, rol FROM Usuarios WHERE correo = ?',
        (email,)).fetchone()
    return cursor


def guardar_usuarios_reg(nombre, correo, contraseña):
    db = get_db()
    db.execute(
        'INSERT INTO Usuarios (nombre,correo,contrasena) VALUES (?,?,?) ',
        (nombre, correo, contraseña)
    )
    db.commit()


def consultar_usuario_g(id):
    db = get_db()
    cursor = db.execute(
        'SELECT idusuarios, nombre, correo, contrasena FROM usuarios WHERE idusuarios = ?',
        (id,)).fetchone()

    return cursor


def consultar_usuario_id(id):
    db = get_db()
    cursor = db.execute(
        'SELECT * FROM usuarios WHERE idusuarios = ?',
        (id,)).fetchall()

    return cursor


def guardar_usuarios_pilot(nombre, email, contraseña, rol):
    db = get_db()
    db.execute(
        'INSERT INTO Usuarios (nombre,correo,contrasena,rol) VALUES (?,?,?,?) ',
        (nombre, email, contraseña, rol)
    )
    db.commit()


def consultar_vuelos_salidas():
    sql = "SELECT * FROM vuelos WHERE origen='Mitu' "
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    vuelos_salida = cursor.fetchall()
    return vuelos_salida


def consultar_vuelos_llegada():
    sql = "SELECT * FROM vuelos WHERE destino='Mitu'"
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    vuelos_llegada = cursor.fetchall()
    return vuelos_llegada


def consultar_vuelos(origen, destino, ida, regreso):
    db = get_db()
    cursor = db.execute('SELECT *  FROM vuelos WHERE origen=? AND destino=? AND fecha_ida=? AND fecha_vuelta=?',
                        (origen, destino, ida, regreso)).fetchall()

    return cursor


def consultar_vuelos_ida(origen, destino, ida):
    db = get_db()
    cursor = db.execute(
        'SELECT *  FROM vuelos WHERE origen=? AND destino=? AND fecha_ida=?',
        (origen, destino,  ida)).fetchall()

    return cursor


def calificar_vuelos(ida, regreso):
    db = get_db()
    cursor = db.execute(
        'SELECT *  FROM vuelos WHERE fecha_ida=? AND fecha_vuelta=?',
        (ida, regreso)).fetchall()

    return cursor


def reservar_vuelos(nombre, apellido, identificacion, email, id_usuario, origen, destino, tipo, ida, regreso, tiquetes, id_vuelo, codigo_vuelo):
    db = get_db()
    db.execute(
        'INSERT INTO reservas (nombre,apellido,identificacion,correo,id_usuario,ciudad_origen,ciudad_destino,tipo_vuelo,fecha_ida,fecha_regreso,n_tiquetes,id_vuelo,codigo_vuelo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ',
        (nombre, apellido, identificacion, email, id_usuario,
         origen, destino, tipo, ida, regreso, tiquetes, id_vuelo, codigo_vuelo)
    )
    db.commit()


def usuarios_consulta():
    sql = "SELECT * FROM usuarios"
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    usuarios = cursor.fetchall()
    return usuarios


def actualizar_usuarios(nombre, email, rol, id):
    db = get_db()
    cursor = db.execute(
        "UPDATE usuarios SET nombre = ?, correo = ?, rol =? WHERE idusuarios = ? ",
        (nombre, email, rol, id))
    db.commit()


def eliminar_usuarios(id):
    db = get_db()
    cursor = db.execute(
        "DELETE FROM usuarios WHERE idusuarios = ? ",
        (id,))
    db.commit()


def consulta_vuelos():
    sql = "SELECT * FROM vuelos"
    conn = sql_connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    vuelos = cursor.fetchall()
    return vuelos


def reservar_vuelos_ida(nombre, apellido, identificacion, email, id_usuario, origen, destino, tipo, ida, tiquetes, id_vuelo, codigo_vuelo):
    db = get_db()
    db.execute(
        'INSERT INTO reservas (nombre,apellido,identificacion,correo,id_usuario,ciudad_origen,ciudad_destino,tipo_vuelo,fecha_ida,n_tiquetes,id_vuelo, codigo_vuelo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ',
        (nombre, apellido, identificacion, email, id_usuario,
         origen, destino, tipo, ida, tiquetes, id_vuelo, codigo_vuelo)
    )
    db.commit()


def consultar_id_vuelo(id):
    db = get_db()
    cursor = db.execute(
        'SELECT * FROM vuelos WHERE idvuelos = ?', (id,)
    ).fetchone()

    return cursor


def agregar_vuelos(origen, destino, estado, numero_vuelo, puerta, hora_salida, hora_llegada, fecha_salida, fecha_vuelta, piloto, avion_asig, capacidad):
    db = get_db()
    db.execute(
        'INSERT INTO Vuelos (origen,destino,estado,numero_vuelo,gate,hora_salida,hora_llegada,fecha_ida,fecha_vuelta,piloto,avion,capacidad) VALUES (?,?,?,?,?,?,?,?,?,?,?,?) ',
        (origen, destino, estado, numero_vuelo, puerta, hora_salida,
            hora_llegada, fecha_salida, fecha_vuelta, piloto, avion_asig, capacidad)
    )
    db.commit()


def actualizar_vuelos(origen, destino, estado, vuelo, gate, hora_salida, hora_llegada, fecha_ida, fecha_vuelta, piloto, avion, capacidad, id):
    db = get_db()
    cursor = db.execute(
        "UPDATE vuelos SET origen = ?, destino = ?, estado =?, numero_vuelo= ?, gate= ?,  hora_salida= ?, hora_llegada= ?,fecha_ida= ?, fecha_vuelta= ?, piloto= ?, avion= ?, capacidad= ? WHERE idvuelos = ? ",
        (origen, destino, estado, vuelo, gate, hora_salida, hora_llegada, fecha_ida, fecha_vuelta, piloto, avion, capacidad, id))
    db.commit()


def eliminar_vuelos(id):
    db = get_db()
    cursor = db.execute(
        "DELETE FROM vuelos WHERE idvuelos = ? ",
        (id,))
    db.commit()


def consultar_piloto_vuelo(id):
    db = get_db()
    cursor = db.execute(
        'SELECT * FROM vuelos WHERE piloto = ?', (id,)
    ).fetchall()

    return cursor


def consultar_reservas(id):
    db = get_db()
    cursor = db.execute(
        'SELECT * FROM reservas WHERE id_usuario = ?', (id,)
    ).fetchall()

    return cursor

