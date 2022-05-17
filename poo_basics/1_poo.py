class Auto:
    
    def __init__(self, marca, color, cantidad_ruedas, velocidad_max):
        self.marca = marca
        self.color = color
        self.cantidad_ruedas = cantidad_ruedas
        self.velocidad_max = velocidad_max
        self.motor = 2.0
        
    def __str__(self):
        return f"{self.motor}, {self.marca}, {self.cantidad_ruedas}, {self.color}, {self.velocidad_max}"
    
    def acelerar(self):
        print(f"El auto a acelerado hasta {self.velocidad_max}")
        
    def frenar(self):
        print(f"El {self.marca} a frenado")
        
aventador = Auto("mitsubishi", "blanco", 4, 320)
huracan = Auto("mitsubishi", "rojo", 4, 300)

print(aventador)
print(huracan)

aventador.acelerar()
huracan.frenar()