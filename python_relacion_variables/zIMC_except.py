
def isfloat(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

h=input("Digame su altura en centimetros\nAltura:")
while isfloat(h)==False:
    print("No es un valor valido")
    h=input("Digame su altura en centimetros\nAltura:")

m=input("Digame su peso en kilos\nPeso:")
while isfloat(m)==False:
    print("No es un valor valido")
    m=input("Digame su peso en kilos\nPeso:")
m=float(m)
h=float(h)/100
print("Su IMC es "+str(round((m/h/h),2)))