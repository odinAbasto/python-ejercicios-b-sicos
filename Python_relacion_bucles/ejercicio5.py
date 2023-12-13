# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
c=float(input("Escriba la cantida a invertir: "))
i=float(input("Escriba el interes anual(%): "))
n=int(input("Escriba el numero de años que dura la inversion: "))

for j in range(1,n+1):
    ci=c*(1+i/100)**j
    print("El año "+ str(j) +" el capital obtenido es de "+str(ci))