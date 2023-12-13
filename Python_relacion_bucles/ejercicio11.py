# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
word=input("Escriba una palabra: ")
for i in range(1,len(word)+1):
    print(word[len(word)-i])