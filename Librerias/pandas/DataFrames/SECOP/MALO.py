import pandas as pd

peajes = pd.read_csv('Peajes_clean.csv', sep=";")

# Descriptivas
categoricas = peajes[['NOMBRE', 'CONCESION', 'GEN', 'SENTIDO', 'COD_VIA', 'DEP', 'CONCESIONA', 'INIC_OPER', 'ETIQUETA']]

numericas = peajes[['CAT1','CAT2','CAT3','CAT4','CAT5','CAT6','CAT7']]

categoricas.info() # Etiqueta,columnas, Count Non-null, Dtype
numericas.info()

categoricas.describe() # Count, Unique, Top, Freq
numericas.describe() # Count, Unique, mean, std, max, 25%, 50%, 75%

categoricas['DEP'].unique() # Unicos Array
categoricas['SENTIDO'].unique() # Unicos Array
categoricas['GEN'].unique() # Unicos Array
categoricas['DEP'].value_counts() # Contar repeticiones

numericas.max() # Maximo
numericas.idxmax() # Etiqueta
