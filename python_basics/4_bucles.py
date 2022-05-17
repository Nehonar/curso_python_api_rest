tabla_a_calcular = int(input("Ingrese la talba que desea calcular: "))
hasta_donde = int(input(f"Hasta que numero desea calcular la tabla de {tabla_a_calcular} :"))
primero = 1

for i in range(hasta_donde):
    print(f"{tabla_a_calcular} x {i+1} = {tabla_a_calcular * (i+1)}")

while primero > hasta_donde:
    print(f"{tabla_a_calcular} x {primero} = {tabla_a_calcular * primero}")
    primero =+ 1