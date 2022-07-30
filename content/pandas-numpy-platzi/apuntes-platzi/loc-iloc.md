# Filtrado con loc e iloc

Cuando queremos ***navegar*** por un dataFrame estas funciones permiten filtrar datos de manera más específica

## .loc

Filtra según un ***label***

```python
import pandas as pd

df_books = pd.read_csv("/content/bestsellers-with-categories.csv")
df_books[:] # Mostrar todas las filas
# Mostrar un rango de filas tomando en cuenta el inicio y el final
df_books[0:4]
# Filtrando por columnas
df_books[["Name","Author"]]
# Filtrando por filas y columnas
df_books.loc[0:4, ["Name", "Author"]]
# Modificar los valores de una columna específica de un DataFrame
df_books.loc[:, ["Reviews"]] * -1
# Filtrar datos que cumplan una condición determinada
df_books.loc[0:4, ["Author"]] == "JJ Smith"
```

## .iloc

Filtra mediante ***índices***.

```python
# Muestra todos los datos del dataframe
df_books.iloc[:]
# Filtrar datos según los índices de las filas y columnas
df_books.iloc[:4,0:3]
# Buscar un dato en específico
df_books.iloc[1,3] # Fila 1, Columna 3
```