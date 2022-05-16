import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')

df_records = df_records[['Nombre', 'Goles']].sort_values('Goles', ascending=False)
print(df_records[  df_records['Goles'] >= df_records['Goles'].quantile(0.75)])
#print(df_records['Goles'].quantile(0.75))