class Curso:
    
    __titulo = "backend python3"
    __duracion = 20
    
    def __adquirir_curso(self):
        print("Has adquirido el curso")
        
    def get_adquirir_curso(self):
        return self.__adquirir_curso()
    
    def get_titulo(self):
        return self.__titulo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo
        
curso = Curso()
curso.get_adquirir_curso()
print(curso.get_titulo())
curso.set_titulo("Backend python pro")
print(curso.get_titulo())
