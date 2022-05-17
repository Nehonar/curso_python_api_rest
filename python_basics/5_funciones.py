def saludar():
    print("Hola que tal")
    
def saludar_persona(persona="Persona generica", *args, **kwargs):
    print(f"Hola {persona}")

saludar()
saludar_persona("Benito")

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def dividir(num1, num2):
    return num1 / num2

def multiplicar(num1, num2):
    return num1 * num2

result = sumar(1, 2)
print(result)
print(sumar(2, 3))

def calcular():
    menu = int(input("""
                 [1] Para sumar
                 [2] Para restar
                 [3] Para dividir
                 [4] Para multiplicar
                 >>>
                 """))

    num1 = int(input("Ingre primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))

    if menu == 1:
        print(sumar(num1, num2))
        
    elif menu == 2:
        print(restar(num1, num2))
        
    elif menu == 3:
        print(dividir(num1, num2))
        
    elif menu == 4:
        print(multiplicar(num1, num2))
    
    elif menu == 5:
        print("Gracias por probarme")
        exit()
    else:
        print("Esa opcion no es validad")

while True:
    calcular()
    
    