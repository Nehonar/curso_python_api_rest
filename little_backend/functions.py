from models import Movie, Genero, Catalog
import sql

catalog = Catalog("Peliculas de mafia")

def add_movie():
    
    name = str(input('Add movie name\n'))
    duration = int(input('Add movie duration\n'))
    genero = int(input('Add movie genero\n'))
    
    movie = Movie(name, duration, genero)
    
    sql.add_movie(movie)

def get_movies():
    
    movies = sql.get_movies()
    for movie in movies:
        save_movie = Movie(
            movie[1],
            movie[2],
            movie[3]
        )
        catalog.movies.append(save_movie)
        
    for movie in catalog.movies:
        print(f"""\
-----------
Movie name: {movie.name}
Movie duration: {movie.duration} minuts
Movie genero: {movie.genero}\n""")
    