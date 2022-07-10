# NumPy Array

El array es el principal objeto de la librería. Representa datos de manera estructurada y se puede acceder a ellos a través del indexado, a un dato específico o un grupo de muchos datos específicos.

```python
import numpy as np

lista = [1,2,3,4,5,6,7,8]

#Volvemos nuestra lista, un array
arr = np.array(lista)

# Una matriz son varios Vectores o listas agrupadas una encima de la otra, 
# es como una tabla de Excel
matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)

# El indexado nos permite acceder a los elementos de los array y matrices
# Los elementos se empiezan a contar desde 0.
arr[0]
matriz[fila][columna]
```

## Slicing

Nos permite extraer varios datos, tiene un comienzo y un final.

```python
# En este ejemplo se está extrayendo datos desde la posición 1 hasta la 5.
arr[1:6]

# Si no se ingresa el valor de inicio, se toma el inicio como la posición 0.
arr[:6]

# En cambio, si no se le da una posición final, se regresan todos 
# los elementos hasta el final del array.
arr[1:]

# También se puede trabajar por pasos.
# En este ejemplo de 3 en 3.
# Regresa la posición 0, 0 + 3, 3 + 3 y como no hay posición 6 + 3, no se regrese nada.
arr[::3]

# Cuando se le asigna un valor negativo se regresan los valores 
# comenzando desde la última posición del array.
arr[-1]
arr[-3:]

# Para el caso de las matrices, sucede algo similar.
# Para acceder a los valores entre filas.
matriz[1:]

# Para acceder a los valores entre filas y columnas.
matriz[1:, 0:2]
```