n=int(input("Escriba un numero y le digo si es primo: "))
primo=True
for i in range(2,n):
    if n%i==0:
        primo=False
    if not primo:
        break

if primo:
    print(str(n)+" es primo")
else:
    print(str(n)+" no es primo")