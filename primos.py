numero = 2000000
suma = 0

for numero in range(2, 2000000):
    es_primo = True


    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False


    if es_primo:
        suma = suma + numero
    else:
        pass


print(suma)
