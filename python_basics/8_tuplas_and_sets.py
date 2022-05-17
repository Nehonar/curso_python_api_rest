tupla = (100, "hello", ["familia", "amigos"], {"hello": "hola"})

print(tupla)
print(tupla[0])
print(tupla[-1])

# convert tuple in list to append new item and convert again in tuple
tupla = list(tupla)
tupla.append(200)
tupla = tuple(tupla)
print(tupla)

nuestro_set = {21 ,19 ,20 ,21}
print(nuestro_set)

