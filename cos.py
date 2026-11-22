#0 = lunes, 1 = martes, 2 = miercoles, 3 = jueves, 4 = viernes, 5 = sabado, 6 = domingo
contador = 0
dias_semana = 0


for año in range (1900, 2001):
    for mes in range (1, 13):
        if mes in [4, 6, 9, 11]:
            dias_mes = 30
        elif mes == 2:
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
                dias_mes = 29
            else:
                dias_mes = 28
        else:
            dias_mes = 31
   
        if dias_semana == 6 and año > 1900:
            contador = contador + 1
       
        dias_semana = (dias_semana + dias_mes) % 7
   
print("Cantidad de domingos que cayeron en primero del mes:", contador)





