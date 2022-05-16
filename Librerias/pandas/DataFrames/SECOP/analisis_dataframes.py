"""
funcion head(n) -> Top n numero de datos
funcion tail(n) -> De abajo n numero de datos 
-info() -> Tipo de dato, non null object
Dtyooe
describe() -> count, unique, top, freq, first, last
"""

import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')

print("INFO".center(50,'-'))
print(df_records.info())
print("DESCRIBE".center(50,'-'))
print(df_records.describe())

#! Unique
print("UNICOS".center(50,'-'))
print(df_records['Nacionalidad'].unique().tolist())

#! Value counts
print("Value counts".center(50,'-'))
print(df_records['Nacionalidad'].value_counts()) # Serie

# !################ ESTADISTICAS ########################
print("Promedio Goles".center(50,'-'))
print(df_records['Goles'].mean())

print("Promedio Asistencias".center(50,'-'))
print(df_records['Asistencias'].mean())

print("Moda nacionalidad".center(50,'-'))
print(df_records['Nacionalidad'].mode())

"""
max() -> Valor maximo
min() -> Valor minimo
idxmax() -> Etiqueta del valor max
idxmin() -> Etiqueta del valor min
quantile(0.5) -> Trabajar con cuartiles
sum() -> Suma de todos los valores de una columna
prod() -> Multiplicar entre si
div(12) -> Dividir entre un valor

! Axis
sum(axis=1) Sumar en eje X
sum(axis=0) Sumar en eje y
"""