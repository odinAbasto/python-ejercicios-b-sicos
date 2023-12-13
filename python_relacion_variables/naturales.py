
#Cambiar punto por numero
#Detecta numeros naturales
def punto(n):
    if n.find(".")!=-1:
        n=n.replace(".","0")
        return n.isdigit()
    elif n.find(",")!=-1:
        n=n.replace(",","0")
    else: 
        return n.isdigit()

n=input("Escriba un numero real: \nn: " )
while punto(n)==False:
    print("Valor no valido")
    n=input("n: " )
print(n+" es un numero real")


#Detecta que sea un numero
# n=input("Escriba un numero cualquiera: \nn: " )
# # if n.find("")
# while not n.isnumeric():
#     print("Valor no valido")
#     n=input("n: " )
# n=int(n)
# print(str(n)+" es un numero")