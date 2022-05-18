"""
Agrupamiento
"""

import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')

df_records['Hermanos'] = df_records['Hermanos'].fillna(0).astype(int)
print(df_records)
# Agrupamiento por nacionalidad
print('Agrupamiento'.center(60,"#"))
por_rama = df_records.groupby('Nacionalidad')

for name, group in por_rama:
  print(name, len(group))

#print(len(por_rama))
inglaterra = por_rama.get_group('Inglaterra')
print(inglaterra)

# Se pueden hacer operaciones sobre grupos