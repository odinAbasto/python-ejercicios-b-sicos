# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contrasena="password123"
valido=False
while not valido:
    password=input("Escriba la contraseña: ")
    if password==contrasena:
        valido=True

    if valido:
        print("La contraseña es correcta!")
    else:
        print("La contraseña es incorrecta")
        
    