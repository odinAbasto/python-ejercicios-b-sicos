
#algoritmo que detecta si un numero es natural o no
def natural(n):
    if n[0] in ("-","+"):
        return n[1:].isdigit()
    return n.isdigit()

n=input("Escriba un numero natural\nn: ")

if natural(n)==False:
    print("No es un numero natural")
else:
    print("Es un numero natural")