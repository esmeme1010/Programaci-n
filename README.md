# ¿CUÁNTOS DOMINGOS CAYERON EN 1ER DIA DEL MES EN EL SIGLO XX?
$\color{green}{\textsf{el programa cuenta cuantos domingos cayeron en primer día de mes durante el siglo XX }}$

## Variables

- `contador`: cuenta los domingos que cayeron en día 1 (empieza en 0),<ins>linea 2,19 </ins>.

- `dias_semana`: día de la semana en que cae el día 1 del mes (0 = lunes, ..., 6 = domingo). Empieza en 0 porque el 1 de enero de 1900 fue lunes, <ins>linea 3,18,21  </ins>.

- `dias_mes`: cuántos días tiene el mes actual (28, 29, 30 o 31),  <ins>linea 9,12,14,16 </ins>.

## Cómo funciona

1. Recorre cada año de 1900 a 2000 y cada mes del 1 al 12.
2. Calcula los días del mes, tomando en cuenta los años bisiestos.
3. Si el día 1 cae en domingo y el año es mayor a 1900, suma 1 al contador.
4. Avanza `dias_semana` con el residuo de dividir entre 7.

## Ejecución
    py.py   > [!guardamos con nombre diferente el mismo código]
    cos.py

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


## Resultado

Cantidad de domingos que cayeron en primero del mes: **171**

## Autor
- $\color{green}{\textsf{Esmeralda Yazmin Mora Franco}}$
- $\color{red}{\textsf{Rubén Omar Jiménez Muñoz}}$