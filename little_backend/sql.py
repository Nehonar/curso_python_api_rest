import sqlite3
from ssl import cert_time_to_seconds

from constantes import DATABASE_NAME

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

def add_movie(movie):
    
    conn, cursor = connect_db()
    
    movie = (
        movie.name,
        movie.duration,
        movie.genero
    )
    
    sql = f"INSERT INTO movie (name, duration, genero) VALUES {movie};"
    cursor.execute(sql)
    
    conn.commit()
    conn.close()