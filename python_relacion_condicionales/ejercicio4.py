# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
n=int(input("Escriba un numero entero: "))
if n%2==0:
    print(str(n) +" es par")
else:
    print(str(n) +" es impar")