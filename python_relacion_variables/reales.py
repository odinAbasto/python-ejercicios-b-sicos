

#Detecta numeros naturales
n=input("Escriba un numero entero: \nn: " )

while not n.isdigit() or  int(n)<=0  :
    print("Valor no valido")
    n=input("n: " )
n=int(n)
print(str(n)+" es un numero entero")


#Detecta que sea un numero
# n=input("Escriba un numero cualquiera: \nn: " )
# # if n.find("")
# while not n.isnumeric():
#     print("Valor no valido")
#     n=input("n: " )
# n=int(n)
# print(str(n)+" es un numero")