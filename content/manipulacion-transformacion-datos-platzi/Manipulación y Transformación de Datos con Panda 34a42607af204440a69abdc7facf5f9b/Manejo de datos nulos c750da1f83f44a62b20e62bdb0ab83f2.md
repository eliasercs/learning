# Manejo de datos nulos

Los datos nulos ***son dolores de cabeza*** para este mundo de la ciencia de datos y se van a encontrar mucho en nuestros DataFrames

```python
import pandas as pd
import numpy as np

# Creamos un DataFrame con algunos valores nulos
data = {"Col1": [1,2,3,np.nan],
				"Col2": [4,np.nan,6,7],
				"Col3": ["a","b","c",None]}

df = pd.DataFrame(data)

# Identificar valores nulos en un DataFrame
df.isnull()

# Identificar valores nulos con un valor numérico
df.isnull()*1

# Sustituir los valores nulos por una cadena
df.fillna("Missing")

# Sustituir valores nulos por una medida estadística realizada 
# con los valores de las columnas
df.fillna(df.mean())

# Sustituir valores nulos por valores de interpolación
df.interpolate()

# Eliminar valores nulos
df.dropna()
```