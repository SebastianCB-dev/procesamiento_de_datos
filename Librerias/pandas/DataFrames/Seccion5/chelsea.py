import pandas as pd

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')
df_records[['Salario','Goles']] = df_records[['Salario','Goles']].div(0.3).round(2)
print(df_records)