# Pivot y Melt

## pivot_table

Esta función puede traer recuerdos a las personas interesadas en el mundo del SQL, ya que Oracle, PostgreSQL y otros motores de bases de datos la tienen implementada desde hace muchos años. Pivot, básicamente, transforma los valores de determinadas columnas o filas en los índices de un nuevo DataFrame, y la intersección de estos es el valor resultante.

Entiendo que esto puede sonar algo confuso, pero no te preocupes, todo queda mucho más claro con un ejemplo.

1. Para comenzar, crea un nuevo Jupyter Notebooks, puedes usar Google Colab o la notebook de tu preferencia que estés utilizando para este curso.
2. Carga el DataFrame que hemos usado en el curso:

```python
df_books = pd.read_csv("/content/bestsellers-with-categories.csv",sep=",",header=0)

# Como resultado, los valores de Author pasan a formar el índice por fila 
# y los valores de Genre pasan a formar parte de los índices por columna, 
# y el User Rating se mantiene como valor.
df_books.pivot_table(index='Author',columns='Genre',values='User Rating')

# Por supuesto, para este caso, un Author suele tener un solo género literario, 
# así que no es una transformación muy útil, pero veamos si podemos lograr algo mejor.

# En este caso tenemos por cada género, la suma a lo largo de los años. 
# Esto es mucho más interesante, ¿verdad? La mejor noticia es que no solo podemos 
# obtener la suma, también podemos obtener la media, la desviación estándar, 
# el conteo, la varianza, etc. Únicamente con cambiar el parámetro 
# aggfunc que traduce función de agrupamiento.
df_books.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum')
```

## melt

El método melt toma las columnas del DataFrame y las pasa a filas, con dos nuevas columnas para especificar la antigua columna y el valor que traía.

Por ejemplo, simplemente al imprimir las cinco primeras filas del DataFrame con las columnas de `Name` y `Genre` se tiene este resultado.

```python
df_books[['Name','Genre']].head(5)

df_books[['Name','Genre']].head(5).melt()

df_books.melt(id_vars='Year',value_vars='Genre')
# Simplemente, podemos seleccionar las columnas que no quiero hacer melt 
# usando el parámetro id_vars. Para este caso Year y también la 
# única columna que quiero aplicar el melt, para este caso Genre 
# con la propiedad value_vars.
```