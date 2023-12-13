# Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#  Si el divisor es cero el programa debe mostrar un error.

x=float(input("Dime un numero: "))
y=float(input("Dime otro numero: "))
if y==0:
    print("Error. El denominador no puede ser cero")
else:
    print("El resultado es "+str(x/y))