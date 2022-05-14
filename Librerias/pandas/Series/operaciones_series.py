import pandas as pd

data_1 = { 1:2, 2:4, 3:8, 4:16, 5:32 }
data_2 = { 1:1, 2:8, 3:27, 4:64, 5:125 }
data_3 = { 1:1, 2:16, 3:81, 4:256, 5:625, 6:1296 }

serie_2 = pd.Series(data_1)
serie_3 = pd.Series(data_2)
serie_4 = pd.Series(data_3)

print(serie_2)
print(serie_3)
print(serie_4)

# !Extraer valores

# 1. Extraer un valor usando la etiqueta
print( serie_2.get(2) ) # Si no existe el índice arroja None

# 2. Extraer valores usando las etiquetas: loc[inicio:fin]
# Se cuenta la etiqueta 'fin'
print( serie_2.loc[2:4] )

# 3. Extraer por posicion: iloc[inicio:fin]
# No se cuenta la posicion 'fin'
print( serie_2.iloc[2:4] )


#! Extraer todos los valores y copiar una serie
print( serie_2.values ) # Retorna un ndarray
print( serie_2.to_list() ) # Retorna un array

#imprimir_valores_serie( serie_2 )

def imprimir_valores_serie( serie: pd.Series ) -> None:
  for num in serie.to_list():
    print(num)
 
nueva_serie = serie_2.copy()

# !Calculos

print( serie_2 + 1 ) # Suma 1 a todos los valores de la serie y retorna una nueva serie

# Suma
# Tener cuidado con el numero de elementos y los indices
print( serie_2 + serie_3 )

print( serie_2 + serie_4 ) # NaN por índice.

# Sumar sin errores
print( serie_2.add(serie_4, fill_value=0) )


# !Operaciones estadísticas

serie_2.max() # Maximo valor
serie_2.min() # Minimo valor
serie_2.mean() # promedio
serie_2.std() # Desviación estandar
serie_2.median() # Mediana

