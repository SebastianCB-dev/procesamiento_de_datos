import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')

print( df_records.info() )

#! Buscar registros nulos
sin_hermanos = df_records[df_records['Hermanos'].isna()]

print(sin_hermanos)

# Convertir str a datetime
# to_datetime()

#! Eliminar nulos
df_records['Hermanos'] = df_records['Hermanos'].fillna(0)

# !Convertir a un dato
df_records['Hermanos'] = df_records['Hermanos'].astype(int)

print(df_records)