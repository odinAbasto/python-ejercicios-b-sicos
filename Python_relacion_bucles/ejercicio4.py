# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

n=input("Escriba un numero entero positivo: \nn: " )

while not n.isdigit():
    print("Valor no valido")
    n=input("n: " )
n=int(n)
output='cuenta atrás: '
for i in range(n,-1,-1):
    output+=str(i)+', '
print(output[:(len(output)-2)])

