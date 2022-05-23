from datetime import datetime
import sqlite3

conexion = sqlite3.connect("DB_curso/base_prueba_curso.db")
cursor = conexion.cursor()
open_menu = True

def get_clients():
    sql = "SELECT * FROM clientes;"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente[1])
        
def add_client():
    nombre = str(input("Digame el nombre\n")) 
    apellido = str(input("Digame el apellido\n")) 
    email = str(input("Digame el email")) 
    fecha_registro = datetime.now()
    telefono = int(input("Digame telefono (OPCIONAL)\n"))
    cliente = (
        nombre,
        apellido,
        email,
        fecha_registro,
        telefono
    )
    sql = f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono) VALUES {cliente}"
    cursor.execute(sql)
    
def get_client(id):
    sql = f"SELECT * FROM clientes WHERE id = {id}"
    cursor.execute(sql)
    cliente = cursor.fetchone()
    print(cliente)

def edit_client(id, edit_param):
    sql = f"UPDATE clientes SET nombre = '{edit_param}' WHERE id = {id}"
    cursor.execute(sql)
    
def delete_client(id):
    sql = f"DELETE FROM clientes WHERE id = {id}"
    cursor.execute(sql)

def open_menu():
    while open_menu:
        option = int(input(
            """
            [1] Watch all clients
            [2] Add new client
            [3] Watch a client
            [4] Edit a client
            [5] Delete a client
            [6] Exit
            """
        ))
        
        if option == 1:
            get_clients()
        elif option == 2:
            add_client()
        elif option == 3:
            get_client()
        elif option == 4:
            edit_client()
        elif option == 5:
            delete_client()
        elif option == 6:
            print("Nos vemos en la proxima")
            exit()
        else:
            print("Lo siento, no a elegido una opción valida")
            


conexion.commit()
conexion.close()