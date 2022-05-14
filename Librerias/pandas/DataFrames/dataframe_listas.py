import pandas as pd

numeros = [9,19,29,11,3]
nombres = ['Romelu Lukaku','Mason Mount','Kai Havertz','Timo Werner','Antonio Rudger']
goles = [13,20,21,16,5]
asistencias = [5,10,8,7,1]
nacionalidades = ["Belgica", "Inglaterra","Alemania", "Alemania","Alemania"]
fechas = ["10/10/1995","11/10/1995","12/10/1995","13/10/1995","14/10/1995"]

datos = {"numero": numeros,
         "nombre": nombres,
         "goles": goles,
         "nacionalidad": nacionalidades,
         "fecha": fechas}

df_chelsea_fc = pd.DataFrame(datos)

print( df_chelsea_fc )