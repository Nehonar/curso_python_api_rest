class Animal:
    
    def __init__(self, edad, numero_de_patas, alimentacion):
        self.edad = edad
        self.numero_de_patas = numero_de_patas
        self.alimentacion = alimentacion
        
    
    def caminar(self):
        print("El animal camina")
        
    def correr(self):
        print("El animal corre")
        
class Perro(Animal):
    raza = None
    ladrido = None
    pelaje = None
    
    def ladrar(self):
        print("GUAU GUAU")
        
    def morder(self):
        print("Mordisco!")
        
class Gato(Animal):
    
    def saltar(self):
        print("El gato salta")
     
perro = Perro(5, 4, "Carnivoro")
perro.raza = "Caniche"
perro.ladrido = "Fuerte"
perro.pelaje = "Blanco"

print(perro.edad)
print(perro.numero_de_patas)
print(perro.alimentacion)
print(perro.ladrido)
print(perro.pelaje)

perro.correr()
perro.caminar()
perro.ladrar()
