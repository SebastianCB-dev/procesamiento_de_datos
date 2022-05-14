# Pandas procesamiento de datos
# Ciencia de datos
# Series y DataFrames

#!Serie
"""
- Muchos registros, ordenados según algún criterio
- Mismo tipo de dato para todas las columnas
- Un nombre que describe la serie
- buena practica: No dejar etiquetas repetidas

Índice |  Temperaturas en Bogotá
  0                 19
  1                 18
  2                 20
  3                 14
  4                 20
  5                 20
"""
"""
Índice |  Temperaturas en Bogotá
  5/11/20           19
  6/11/20           18
  7/11/20           20
  8/11/20           14
  9/11/20           13
  10/11/20          17
"""

# ! Importar pandas
import pandas as pd

datos = [1, 3, 29, 19, 11, 9, 10]

#! Crear Series
jugadores_chelsea = pd.Series(datos, name="Jugadores Chelsea F.C.")

print(jugadores_chelsea)

#! Tipos

print( type(jugadores_chelsea) )
print( type(jugadores_chelsea.values) )
print( jugadores_chelsea.dtypes )




