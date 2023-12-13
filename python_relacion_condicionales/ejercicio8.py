# En una determinada empresa, sus empleados son evaluados al final de cada año. 
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, 
# traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden 
# ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se 
# muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida 
# en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	0.4
# Meritorio	0.6 o más
# Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
# así como la cantidad de dinero que recibirá el usuario.

pun=float(input("Indique una puntucacion: "))
if pun==0.0:
    print("Su rendimiento es inaceptable")
    print("No recibirá nada")
elif pun==0.4:
    print("Su rendimiento es aceptable")
    print("Recibirá "+str(2400.0*pun)+" euros")
elif pun>=0.6 and pun<=1:
    print("Su rendimiento es meritorio")
    print("Recibirá "+str(round(2400.0*pun,2))+" euros")
else:
    print("Puntuación no válida")