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
        