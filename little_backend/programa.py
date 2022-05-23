import funciones

while True:
    menu = int(input("[1] Add new movie\n[2] Obtain movies\n[0] Exit menu\n>>> "))
    
    if menu == 1:
        funciones.add_movie()
    elif menu == 2:
        pass
    elif menu == 0:
        print('See you next time...')
        exit()