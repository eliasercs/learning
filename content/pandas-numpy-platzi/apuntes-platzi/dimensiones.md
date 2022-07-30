# Dimensiones

Con las matrices podemos crear varias dimensiones, vamos a nombrarlas

- **Scalar**: 0 Un solo dato o valor
- **Vector**: Listas de Python
- **Matriz**: Hoja de cálculo (2 dimensiones, filas y columnas)
- **Tensor**: Series de tiempo o Imágenes (Más de dos dimensiones)

```python
import numpy as np

scalar = np.array(42)

# .ndim Nos muestra las dimensiones que tiene 
scalar.ndim

# Declarando un vector
vector = np.array([1, 2, 3])
print(vector) 
vector.ndim

# Declarando una matriz
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
matriz.ndim

# Declarando un tensor
tensor = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], 
	[10, 11, 12]],[[13, 13, 15], [16, 17, 18], 
	[19, 20, 21], [22, 23, 24]]])
print(tensor)
tensor.ndim

# Se puede definir el número de dimensiones desde la declaración del array
vector = np.array([1, 2, 3], ndmin = 10)

# Se pueden expandir dimensiones a los array ya existentes con expand_dims(). 
# Axis = 0 hace referencia a las filas, mientras que axis = 1 a las columnas.
expand = np.expand_dims(np.array([1, 2, 3]), axis = 0)

# Remover/comprimir las dimensiones que no están siendo usadas.
np.squeeze(vector)
```