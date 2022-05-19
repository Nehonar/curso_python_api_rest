nombre_volatil = "Benito"
nombre = str(input("Ingrese su nombre"))
print(nombre)

def leer_fichero():
    
    file = open("file.txt", "r")

    dato = file.read()
    file.close()
    print(dato)

def escribir_ficheros():
    file = open('file.txt', 'w')

    dato = "Mi apellido es Avila"

    file.write(dato)

    file.close()
    
leer_fichero()

file = open('file.txt', 'a')
dato = "\nEsta linea es nueva y la estoy agregando sin borrar nada"
file.write(dato)
file.close()

leer_fichero()
