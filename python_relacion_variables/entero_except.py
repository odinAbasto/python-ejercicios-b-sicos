
#algoritmo que detecta si un numero es real o no
 
def isInt(str):
    try:
        int(str)
    except ValueError:
        return False
    return True

n=input("Escriba un numero entero\nn: ")

while(isInt==False):
    print("Valor no valido!")
    n=input("Escriba un numero entero\nn: ")

print("Eso si es un numero entero")