"""
Hacer un programa que le pida al usuario que ingrese su edad y su sexo,
si el usuario es mayor de edad y ademas es menor de 65 años, le debe permitir
al usuario quedarse en el programa, en caso contrario, el programa debe deternse.
Si el sexo es masculino, el programa saludara al usuario como un caballero y si
el sexo es femenino que el programa salude al usuario como una dama
- para que el usuario ingrese su sexo hacer un menu con condiciones
"""

edad = int(input("Que edad tienes?\n"))
incorrect_answer = True

if edad >= 18 and edad < 65:
    while incorrect_answer:
        sexo = int(input("""
            Cual es tu sexo?
            [1] Masculino
            [2] Femenino
            [3] Indefinido

            Debe escribir un numero\n
        """))
        if sexo in [1, 2, 3]:
            incorrect_answer = False
        else:
            print("ASEGURESE DE PONER EL NUMERO CORRECTO\n\n")

    nombre = str(input("Cual es su nombre?\n"))
    if sexo == 1:
        print(f"Bienvenido {nombre}")
    elif sexo == 2:
        print(f"Bienvenida {nombre}")
    else:
        print(f"Bienvenid@ {nombre}")
else:
    print("Lo sentimos, no puedes participar")