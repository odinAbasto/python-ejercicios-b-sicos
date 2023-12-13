n=input("Escriba un numero entero positivo: \nn: " )

while not n.isdigit():
    print("Valor no valido")
    n=input("n: " )
n=int(n)

for i in range (1,n+1):
    output=''
    for j in range (1,i+1):
        output+='*'
    print(output)
