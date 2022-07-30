# Apply

`Apply`Es un comando muy poderoso que nos deja aplicar funciones a nuestro DataFrame

```python
df_books = pd.read_csv("/content/bestsellers-with-categories.csv")
df_books.head(2)

# Definir una función
def two_times(value):
  return value * 2

# Aplicar la función sobre la columna User Rating
df_books["User Rating"].apply(two_times)

# Se pueden aplicar funciones lambdas
df_books["Price"].apply(lambda x: x*2)

# Apply en varias columnas con condiciones, hay que especificar 
# a que los vamos a aplicar (filas o columnas)
df_books.apply(lambda x: x['User Rating'] * 2 if x['Genre'] == 'Fiction' 
		else x['User Rating'], axis = 1)
```