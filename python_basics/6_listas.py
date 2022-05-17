nombres = [
    "Benito",
    "Mireia",
    "Kyubi",
    "Orion",
]

edades = [
    36,
    34,
    1,
    1,
]

apellidos = [
    ["Avila", "Arroyo"],
    ["Plata", "Pascual"],
    ["Kurama"],
    ["Coco"]
]

print(nombres)

# add name in nombres list
nombres.append("Nathe")
print(nombres)

# remove last element in nombres list
nombres.pop()
print(nombres)

# cantidad de datos en lista
cantidad_de_nombres = len(nombres)
print(f"Cantidad de elementos: {cantidad_de_nombres}")

# last element
print(nombres[-1])

# varios elementos
print(nombres[0, 3])

# primer elemento de primer lista
print(apellidos[0][0])

# numero mas grande de lista
print(max(edades))