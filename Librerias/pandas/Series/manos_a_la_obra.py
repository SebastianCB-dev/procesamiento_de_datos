import pandas as pd
import random

def subir_notas(notas: pd.Series) -> pd.Series:
  if notas.mean() > 2.5:
    notas = notas + round(notas.std(), 2)
    
  for i in range(notas.size):
    nota_actual = notas.iloc[i]
    if nota_actual > 5.0:
      notas.iloc[i] = 5.0
  
  return notas

  


