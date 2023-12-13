# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba "salir" que terminará.
print("Escriba 'salir' para finalizar")
word=""
while word!="salir":
    word=input("escriba lo que quiera: ")
    print(word)