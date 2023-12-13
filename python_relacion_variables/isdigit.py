#SOLO DETECTA SI EL STRING ESTÁ COMPUESTO POR DIGITOS NUMERICOS
#Detecta numeros naturales
n=input("Escriba un numero isdigit: \nn: " )

while not n.isdigit():
    print("Valor no valido")
    n=input("n: " )
n=int(n)
print(str(n)+" es isdigit")


#Detecta que sea un numero
# n=input("Escriba un numero cualquiera: \nn: " )
# # if n.find("")
# while not n.isnumeric():
#     print("Valor no valido")
#     n=input("n: " )
# n=int(n)
# print(str(n)+" es un numero")