

#Detecta numeros naturales
n=input("Escriba un numero entero: \nn: " )
i=n.find(".")
n=n.replace(".","0")
print(i)
print(n)
print(str(n.isdigit()))
#Detecta que sea un numero
# n=input("Escriba un numero cualquiera: \nn: " )
# # if n.find("")
# while not n.isnumeric():
#     print("Valor no valido")
#     n=input("n: " )
# n=int(n)
# print(str(n)+" es un numero")