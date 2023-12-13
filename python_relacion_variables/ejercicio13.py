# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al 
# balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
# depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar 
# por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


c0=float(input("Digame la cantidad invertida: "))
i=4
print("El capital final del año 1 es "+str(round((c0*(1+i/100)**1),2))+" euros")
print("El capital final del año 2 es "+str(round((c0*(1+i/100)**2),2))+" euros")
print("El capital final del año 3 es "+str(round((c0*(1+i/100)**3),2))+" euros")