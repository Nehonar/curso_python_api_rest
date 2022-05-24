class Movie:
   
   def __init__(self, name, duration, genero):
       self.name = name
       self.duration = duration
       self.genero = genero
       
class Genero:
    
    def __init__(self, name):
        self.name = name
        
class Catalog:
    
    def __init__(self, name):
        self.name = name
        self.movies = []