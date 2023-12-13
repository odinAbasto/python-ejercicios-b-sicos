

#Detecta numeros naturales
def comprobarSigno(n):
    if n[0] in ("-","+"):
        return n[1:].isdigit()
    return n.isdigit()

n=input("Escriba un numero entero: \nn: " )

while(comprobarSigno(n))==False:
    print("No es entero")
    n=input("Escriba un numero entero: \nn: " )

print(n+" es un numero entero")