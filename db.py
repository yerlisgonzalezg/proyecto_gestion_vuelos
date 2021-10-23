import sqlite3
from sqlite3 import Error
from flask import current_app, g


def get_db():
    try:
        if 'db' not in g:
            print('conectada')
            g.db = sqlite3.connect('bd_vuelos.db')
        return g.db
    except Error:
        print(Error)


def close_db():
    db = g.pop( 'db', None )

    if db is not None:
        db.close()        

def sql_connection():
    try:
        conn=sqlite3.connect('bd_vuelos.db')
        return conn
    except Error:
        print(Error)
        
def consultar_vuelos_salidas():
    sql= "SELECT * FROM vuelos WHERE origen='Mitu' "
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute(sql)
    vuelos_salida=cursor.fetchall()
    return vuelos_salida

def consultar_vuelos_llegada():
    sql= "SELECT * FROM vuelos WHERE destino='Mitu'"
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute(sql)
    vuelos_llegada=cursor.fetchall()
    return vuelos_llegada


def consultar_total_operaciones():
    sql= "SELECT count(idvuelos) FROM vuelos "
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute(sql)
    operaciones=cursor.fetchone()
    return operaciones

def consultar_total_llegadas():
    sql= "SELECT count('idvuelos') FROM vuelos WHERE destino='Mitu'"
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute(sql)
    llegadas=cursor.fetchone()
    return llegadas

def consultar_total_salidas():
    sql= "SELECT count('idvuelos') FROM vuelos WHERE origen='Mitu'"
    conn=sql_connection()
    cursor=conn.cursor()
    cursor.execute(sql)
    salidas=cursor.fetchone()
    return salidas