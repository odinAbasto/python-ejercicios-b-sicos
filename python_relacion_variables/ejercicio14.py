# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace 
# por no ser fresca y el coste final total.

precio=3.49
ndbda=int(input("Escriba el numero de barras de pan vendidas que no son del dia: ")) 
ndbt=int(input("Escriba el numero total de narras de panel vendidas: "))
print("El precio habitual de una barra de pan es 3.49 euros")
print("Se realiza un descuento de "+str(round((precio*0.60),2))+" euros a las barras de pan que no son frescas")
print("El coste total final es de "+str(ndbda*precio*0.433

+(ndbt-ndbda)*precio)+ " euros")
