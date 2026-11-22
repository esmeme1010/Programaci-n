# ¿CUANTOS DOMINGOS CAYERON EN 1ER DIA DEL MES EN EL SIGLO XX?
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
    py.py
    cos.py


## Resultado

Cantidad de domingos que cayeron en primero del mes: **171**

## Autor
$\color{green}{\textsf{Esmeralda Yazmin Mora Franco}}$
$\color{red}{\textsf{Rubén Omar Jiménez Muñoz }}$
