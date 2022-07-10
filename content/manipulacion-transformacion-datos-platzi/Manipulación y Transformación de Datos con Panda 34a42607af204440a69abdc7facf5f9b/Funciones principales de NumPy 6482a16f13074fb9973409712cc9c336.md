# Funciones principales de NumPy

```python
import numpy as np

arr = np.random.randint(1, 20, 10)
matriz = arr.reshape(2,5)

# .max Para el valor máximo
arr.max()
# Podemos regresar los máximos de cada fila o columna especificando el eje
# 0 -> Columnas
# 1 -> Filas
matriz.max(1)
matriz.max(0)
# También tenemos .argmax() que nos devuelve la posición del elemento
arr.argmax()
# En el caso de la matriz nos muestra con un 1 dónde se encuentra 
# el mayor entre las columnas
matriz.argmax(0) # array([0, 1, 1, 0, 1])

# De forma análoga tenemos .min()
arr.min()

# Podemos saber la distancia entre el valor más bajo con el más alto.
arr.ptp() # 17 - 3 ---> 14
```

### Análisis estadístico

```python
arr.sort() # Ordenar los elementos
np.percentile(arr, 50) # Obtener un percentil
np.median(arr) # Mediana
np.std(arr) # Desviación estándar
np.var(arr) # Varianza
np.mean(arr) # Promedio

a = np.array([[1,2], [3,4]])
b = np.array([5, 6])

# Se pueden unir dos arrays
np.concatenate((a,b), axis = 0)

# ValueError: all the input arrays must have same number of dimensions, 
# but the array at index 0 has 2 dimension(s) and the array at 
# index 1 has 1 dimension(s)

# El error anterior es debido a que ‘a’ tiene 2 dimensiones, mientras que ‘b’ tiene 1.
a.ndim # 2
b.ndim # 1

# Debemos poner ‘b’ en 2 dimensiones también.
b = np.expand_dims(b, axis = 0)
np.concatenate((a,b), axis = 0)

# De igual manera, podemos agregarlo en el otro eje
np.concatenate((a,b), axis = 1)

# ValueError: all the input array dimensions for the concatenation axis 
# must match exactly, but along dimension 0, the array at index 0 has size 2 
# and the array at index 1 has size 1

# Como ‘b’ es una fila y no una columna, no se puede concatenar 
# a menos que se aplique la transpuesta.
# La transpuesta pone nuestro array en sentido opuesto, 
# si el array original es (1,2), con la transpuesta quedará (2,1)
np.concatenate((a,b.T), axis = 1)
```