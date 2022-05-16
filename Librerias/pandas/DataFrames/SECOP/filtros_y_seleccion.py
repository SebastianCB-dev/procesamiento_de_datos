import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')

# ordenadar por goles y las etiquetas cambian
ordenados = df_records.sort_values('Goles')

#print(ordenados)

# !Extraer información

# Por posición
# ordenados.iloc[5] # Unico valor
# ordenados.iloc[5:10] # Rango

# Etiqueta o indice
# ordenados.loc[5] # Etiqueta 5
# ordenados.loc[5:10] # Rango de etiquetas

# ordenados.loc[5:10, ['GOLES']]

# ! ---------------- Selección con condición -----------------

df_records['Nacionalidad'] == 'Inglaterra'

print( df_records[df_records['Nacionalidad'] == 'Inglaterra'] )

# & = AND , | = OR , >, >= , <=, <
print( df_records[(df_records['Nacionalidad'] == 'Inglaterra') | 
                  (df_records['Nacionalidad'] == 'Alemania')])        

# ! ISIN
# Valores de columna

"""
categoricos[categoricos['Sector'].isin(['Servicio Público','deportes')]
"""
                  


  


