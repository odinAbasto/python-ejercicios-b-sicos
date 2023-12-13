n=int(input("Escriba un numero entero positivo: " ))

for i in range (1, n+1):
    output = ''
    for j in range (i,0,-1):
        if j%2 != 0: 
            output += str(j) + ' '
    if i%2 != 0:
        print(output)
