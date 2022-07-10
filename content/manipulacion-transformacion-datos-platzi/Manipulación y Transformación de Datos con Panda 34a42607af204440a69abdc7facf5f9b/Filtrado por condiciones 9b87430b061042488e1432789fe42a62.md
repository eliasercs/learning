# Filtrado por condiciones

**Funciona por lógica booleana** y retorna los valores que están en “True”. Es muy útil porque en ocasiones queremos filtrar o separar datos.

```python
import pandas as pd
import numpy as np

df_books = pd.read_csv("/content/bestsellers-with-categories.csv")
df_books.head(2)

# Mostrar datos que sean mayores a cierto valor
mayor_a_2016 = df_books["Year"] > 2016

# Filtrar datos en nuestro DataFrame que sean mayores a cierto valor
df_books[mayor_a_2016]

# Filtrado con varias condiciones
df_books[genreFiction & mayor2016]

# Filtrado con negación
df_books[~mayor2016]
```