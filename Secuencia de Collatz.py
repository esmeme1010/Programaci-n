mayor = 0 
numero_mayor = 0 
for a in range (1, 1000000):
    n = a
    contar = 1

while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1


    contar = contar + 1
if contar > mayor:
    mayor = contar
    numero_mayor = a

print("Numero inicial:", numero_mayor)
print("Cantidad de numeros:", mayor)