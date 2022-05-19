
class Arma:
    def __init__(self, balas, peso):
        self.balas = balas
        self.peso = peso
        
        
    def disparar(self):
        print("El arma dispara")
        

class Pistola(Arma):
    
    def disparar(self):
        print("El arma dispara lento")
        
class Ametralladora(Arma):
    
    def disparar(self):
        print("El arma dispara rapido")
    
    
arma = Arma(15, 7)
arma.disparar()
pistola = Pistola(12, 5)
pistola.disparar()
ametralladora = Ametralladora(30, 10)
ametralladora.disparar()