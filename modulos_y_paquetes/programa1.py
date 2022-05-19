nombre = "Benito"
edad = 36

def saludar(nombre):
    return f"Hola {nombre}"

class Usuario:
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.premium = False
        
    def premium(self):
        self.premium = True