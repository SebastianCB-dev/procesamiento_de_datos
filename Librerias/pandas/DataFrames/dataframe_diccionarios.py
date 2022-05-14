"""
Muchos registros ordenados según algún criterio
Varias columnas con nombre
Diferentes tipos de datos por columnas
"""
import pandas as pd

a1 = {"Numero": 9, "Nombre": "Romelu Lukaku", "Goles": 13, "Nacionalidad": "Belgica", "Fecha": "12/12/1990", "Asistencias": 5}
a2 = {"Numero": 19, "Nombre": "Mason Mount", "Goles": 20, "Nacionalidad": "Inglaterra", "Fecha": "13/12/1990", "Asistencias": 10}
a3 = {"Numero": 29, "Nombre": "Kai Havertz", "Goles": 21, "Nacionalidad": "Alemania", "Fecha": "14/12/1990", "Asistencias": 8}
a4 = {"Numero": 11, "Nombre": "Timo Werner", "Goles": 16, "Nacionalidad": "Alemania", "Fecha": "15/12/1990", "Asistencias": 7}
a5 = {"Numero": 3, "Nombre": "Antonio Rudger", "Goles": 5, "Nacionalidad": "Alemania", "Fecha": "16/12/1990", "Asistencias": 1}

jugadores = [a1, a2, a3, a4, a5]

#! Crear dataframe
chelsea_fc = pd.DataFrame(jugadores)

print( chelsea_fc )




