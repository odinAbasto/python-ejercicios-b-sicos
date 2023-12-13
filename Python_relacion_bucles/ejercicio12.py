# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
word=input("Escriba un palabra: ")
letter=input("Escriba una letra: ")
while len(letter)!=1:
    letter=input("Escriba solo una letra: ")
count=0
for i in range (0,len(word)):
    if word[i]==letter:
        count+=1
print("La letra "+letter+" se repite "+str(count)+" veces en la frase que ha escrito")