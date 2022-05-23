import sqlite3

from constantes import DATABASE_NAME

def connectar_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

connectar_db()