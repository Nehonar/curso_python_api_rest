ingles = {
    "hello": "hola",
    "day": "dia",
}

print(ingles)
# call a element of diccionary
print(ingles["hello"])

# change element of diccionary
ingles["hello"] = "salut"
print(ingles["hello"])

# add new element
ingles["night"] = "noche"
print(ingles["night"])

# delete elelemt
del(ingles["night"])
print(ingles)

# maths
ingles["diez"] = 10
print(ingles["diez"] + 1)

for palabra in ingles:
    print(palabra)
    
for clave in ingles:
    print(ingles[clave])
    
for key, value in ingles.items():
    print(f"Key: {key}, value: {value}")
    
producto = {
    "id": 2,
    "nombre": "Nevera",
    "precio": 2000,
    "stock": 20,
}
# javascript object notation >>> json
