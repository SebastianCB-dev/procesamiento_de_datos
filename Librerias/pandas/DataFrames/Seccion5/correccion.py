import pandas as pd
import numpy as np

df = pd.DataFrame([{"numero": np.nan,
                    "fecha": pd.NaT,
                    "cadena": None}])

print( df )
print('Info'.center(50,'-'))
print( df.info() )
print('ISNA'.center(50,'-'))
# Esta vacio?
print(df.isna())



