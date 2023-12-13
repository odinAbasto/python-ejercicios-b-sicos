
#algoritmo que detecta si un numero es real o no
 
def isfloat(str):
    if str.find(",")!=-1:
        str=str.replace(",",".")
    try: 
        float(str)
    except ValueError: 
        return False
    return True

n=input("escriba un numero\nn:")
while isfloat(n)==False:
    print("valor no valido")
    n=input("escriba un numero\nn:")
print("Este si es un numero real")