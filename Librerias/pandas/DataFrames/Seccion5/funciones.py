import pandas as pd

def convertir_a_dolares(numero: float) -> int:
  return round(numero / 3600)

df_records = pd.read_csv('Chelsea_CSV_DataFrame.csv')
df_records['Hermanos'] = df_records['Hermanos'].fillna(0).astype(int)

#! aplicar funcion una columna APPLY
df_records['Salario'] = df_records['Salario'].apply(convertir_a_dolares)

# !Lambdas
f = lambda numero: round(numero / 3600)
df_records['Salario'] = df_records['Salario'].apply(f)
df_records['Salario'] = df_records['Salario'].apply(lambda numero: round(numero / 3600))

# !Ternario
val = 400
resultado = "Si" if val > 10 else "No"
print("El resultado es: ", resultado)



print(df_records)




