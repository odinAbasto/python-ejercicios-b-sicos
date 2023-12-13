
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla: La división resultande de dividir
#  <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
#  y <c> y <r> son el cociente y el resto de la división entera respectivamente.

print("Escriba dos numeros enteros: ")
n=int(input("n: " ))
m=int(input("m: " ))
print("La división resultande de dividir "+ str(n) +" entre " +str(m)+ " da un cociente " +str(n//m) +" y un resto " +str(n%m))