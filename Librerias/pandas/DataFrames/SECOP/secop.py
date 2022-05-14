import pandas as pd

# Lectura archivo CSV

df_secop = pd.read_csv('SECOP.csv')

print(df_secop.columns)

# Especificar columnas que se quieren

columnas_valores = ['Valor del Contrato', 'Valor de pago adelantado', 'Valor Pendiente de Pago', 'Valor Pagado']

valores = df_secop[columnas_valores].copy()

print(valores)