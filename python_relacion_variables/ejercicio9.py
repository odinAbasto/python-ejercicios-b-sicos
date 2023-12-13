# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de 
# masa corporal calculado redondeado con dos decimales.
altura=float(input("Cual es su altura?[m]"))
peso=input("Cual es su peso?[kg]: ")
clean_peso=peso.replace(".","")

imc=peso/altura/altura
imc=round(imc,2)
print("Su IMC es "+str(imc))