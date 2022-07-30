# Agregar o eliminar registros

Muchas ocasiones necesitamos agregar, eliminar o separar datos y pandas nos ofrece varias funciones para que este proceso se vuelva mucho más sencillo.

```python
import pandas as pd
import numpy as np

# Muestra las primeras 2 filas del dataframe
df_books = pd.read_csv("/content/bestsellers-with-categories.csv")
df_books.head(2)
# Elimina la columna Genre de la salida, pero no del DataFrame
df_books.drop("Genre",axis=1)
# Elimina la columna Genre del DataFrame
df_books.drop("Genre",axis=1, inplace=True)
# Eliminar una columna
del df_books["Price"]

# Elimina un conjunto de filas a partir de un rango
df_books.drop(range(0,10),axis=0)

# Agrega una nueva columna con valores NaN
df_books["Nueva Columna"] = np.nan

# Mostrar número de filas y columnas
df_books.shape[0]

data = np.arange(0,df_books.shape[0])
# Crear una nueva columna y agregar los valores almacenados en el array
df_books["Rango"] = data

# Para añadir filas se utiliza la función append de Python añadiendo como parámetro 
# una lista, diccionario o añadiendo los valores manualmente.
df_books.append(df_books)
```