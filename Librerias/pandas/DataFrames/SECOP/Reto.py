import pandas as pd

def mejores_estudiantes(estudiantes: pd.Series) -> pd.Series:
  nombres = estudiantes['nombre'].tolist()
  notas = estudiantes[['matematicas','ingles','ciencias','literatura','arte']]
  suma = notas.sum(axis = 1)
  promedio = suma.div(5.0)
  data = {"nombre": nombres, "promedio": promedio}
  nuevo_dataframe = pd.DataFrame(data).sort_values('promedio', ascending=False)
  quartil = nuevo_dataframe[ nuevo_dataframe['promedio'] > nuevo_dataframe['promedio'].quantile(0.75)]
  return quartil



