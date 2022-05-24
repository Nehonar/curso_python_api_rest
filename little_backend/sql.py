import sqlite3

from settings import DATABASE_NAME

def connect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    return conn, cursor

def add_movie(movie):
    """
    Add movie in DB movie
    
    Args:
        movie (): 
            name,
            duration,
            genero
    """
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
    
def get_movies():
    """
    Get all movies in DB
    
    Returns:
        _tople_: (
            id, 
            name, 
            duration, 
            genero
        ) 
    """
    conn, cursor = connect_db()
    
    sql = "SELECT * FROM movie;"
    cursor.execute(sql)
    movies = cursor.fetchall()
    conn.close()
    
    return movies