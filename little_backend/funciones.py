from modelos import Movie, Genero, Catalog
import sql

def add_movie():
    
    name = str(input('Add movie name\n'))
    duration = int(input('Add movie duration\n'))
    genero = int(input('Add movie genero\n'))
    
    movie = Movie(name, duration, genero)
    
    sql.add_movie(movie)