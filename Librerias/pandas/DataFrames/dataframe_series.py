import pandas as pd

tiempos = pd.Series([1,2,3,4,5])
atletas = pd.Series(['a', 'b','c','d','e'])
paises = pd.Series(['f', 'g','h','i','j'])
hola_mundo = pd.Series(['k', 'l','m','n','o'])

datos_series = {"tiempo": tiempos, "atleta": atletas, "pais": paises, "hola_mundo": hola_mundo}

df_records = pd.DataFrame(datos_series)

print(df_records)