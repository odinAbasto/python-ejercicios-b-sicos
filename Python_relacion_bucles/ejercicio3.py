# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
n=input("Escriba un numero entero positivo: \nn: " )

while not n.isdigit():
    print("Valor no valido")
    n=input("n: " )
output='los impares son: '
n=int(n)
for i in range(1,n+1):
    if i%2!=0:
        output+=str(i)+', '
print(output[:(len(output)-2)])
