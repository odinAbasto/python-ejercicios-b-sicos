# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.

# Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. 
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de 
# su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir
#  un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
#  Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

eleccion=0 
while eleccion!=1 and eleccion!=2:
    eleccion=input("\n\n\nSeleccione pitsa vegetariana(pulse 1) o no vegetariana(pulse 2):")
    if eleccion.isnumeric():
        if int(eleccion)==1:
            eleccion=1
        elif int(eleccion)==2:
            eleccion=2

print()
todas=["Mozarella", "Tomate"]
veg=["Pimiento", "Tofu"]
noveg=["Peperoni", "Jamon", "Salmón"]
if eleccion==2:
    ingr=0
    while ingr!=1 and ingr!=2 and ingr!=3:
        print ("Elija un ingrediente(Pulse 1, 2 o 3):")
        print("1. Peperoni")
        print("2. Jamon")
        print("3. Salmon")
        aux=input("choice: ")
        if not aux.isnumeric():
            print("¡Elección no valida!")
        else:
            ingr=int(aux)
else:
    print ("Elija un ingrediente(Pulse 1 o 2):")
    print("1. Pimiento")
    print("2. Tofu")
    ingr=0
    while ingr!=1 and ingr!=2:
        aux=input("choice: ")
        if not aux.isnumeric():
            print("¡Elección no valida!")
        else:
            ingr=int(aux)

print()
if eleccion==2:
    
    print("La pizza elegida es NO vegana")
else:
    print("La pizza elegida es vegana")

print("Los ingredientes que lleva son:")

for i in range(len(todas)):
    print ("    "+todas[i])

if eleccion==2:
    print("    "+noveg[int(aux)-1])
else:
    print("    "+veg[int(aux)-1])