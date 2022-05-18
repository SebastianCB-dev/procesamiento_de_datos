import pandas as pd

df_records = pd.read_csv('Examen.csv')

df_records = df_records.sort_values(by='MODELO')
# print(df_records)
# nombres = df_records['MODELO'].unique().tolist()
descargas_agrup=df_records.groupby(by=['MODELO'])
def comentarios(z):
  return len(z[z['COMENTARIO'] == True])
result = descargas_agrup.apply(comentarios)#.groupby('MODELO').sum()['COMENTARIO']
print(result.tolist())
# array_comentarios = []
# for nombre in nombres:
#   numero = df_records[ (df_records['MODELO'] == nombre ) & 
#                        (df_records['COMENTARIO'] == True)]
#   array_comentarios.append(len(numero))
# array_valores = [1] * 15
# df_records['COMENTARIO'] = array_comentarios


# print(df_records)