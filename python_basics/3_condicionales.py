nombre = str(input("Como te llamas?\n"))
edad = int(input("Que edad tienes?\n"))

persona_masculina = False
persona_femenina = False
finalizar_bucle = True
while finalizar_bucle: 
    persona_masculina = str(input("Eres masculino?\n"))
    if persona_masculina == "si":
        persona_masculina = True
        finalizar_bucle = False
    elif persona_masculina == "no":
        persona_femenina = True
        finalizar_bucle = False
    else:
        print("Responda con si o no, pro favor")

# Comparación de nombres
if nombre == "Benito":
    print("El nombre es Benito")
elif nombre == "Mireia":
    print("El nombre es Mireia")
elif nombre == "Kyubi" or nombre == "Orión":
    print("Eres el gato!")
else:
    print("No te conozco")

# Comparación de edades
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Comparación de booleanos
if persona_masculina and not persona_femenina:
    print("Se cumplen las dos")
else:
    print("No se cumple ninguna")

if persona_masculina:
    print("Persona masculina")
