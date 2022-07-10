# groupby

Permite **agrupar datos en función de los demás**. Es decir, hacer el análisis del DataFrame en función de una de las columnas.

```python
import pandas as pd

df_books = pd.read_csv("/content/bestsellers-with-categories.csv",sep=",",header=0)

# Agrupar por Author y mostrar el conteo de los datos de las demás columnas
df_books.groupby("Author").count()

# Agrupar por Author y mostrar la media de los datos de las demás columnas
df_books.groupby("Author").median()

# La columna Author, en los casos anteriores, pasa a ser el índice.
# Podemos usar loc y acceder a un dato específico del DataFrame. 
# Agrupar por autor y mostrar la suma de los valores de las demás columnas 
# para William Davis
df_books.groupby("Author").sum().loc["William Davis"]

# Agrupar por author y mostrar la suma de los valores de las demás columnas. 
# Colocar los índices que el DataFrame trae por defecto
df_books.groupby("Author").sum().reset_index()

# La función agg() permite aplicar varias funciones al DataFrame una vez agrupado 
# según una columna específica. Agrupar por Author y mostrar el mínimo y máximo 
# de las demás columnas
df_books.groupby("Author").agg(["min","max"])

# Agrupar por Author, obtener el mínimo y máximo de la columna 
# ‘Reviews’ y sumar los valores de la columna ‘User Rating’
df_books.groupby('Author').agg({'Reviews':['min','max'], 'User Rating':'sum'})

# Agrupar por ‘Author - Year’ y contar los valores de las demás columnas
df_books.groupby(['Author','Year']).count()
```