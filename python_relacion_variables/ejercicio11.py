# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

cantidad=float(input("¿Qué cantidad desea invertir?: "))
interes=float(input("¿Cual es el interes anual?: "))
n=int(input("¿Cuanto años dura la inversión?: "))
print("El capital obtenido es de "+str(cantidad*(1+n*interes/100))+" euros")
