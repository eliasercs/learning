# Shape y Reshape

Hay 2 funciones muy importantes de los arreglos (Shape y Reshape). La forma de un arreglo nos va a decir con que **estructura** se está trabajando (tamaño, manipular, ingresar).

### Shape

```python
import numpy as np

arr = np.random.randint(1,10,(3,2))

# [[4, 2],
#  [4, 8],
#  [4, 3]]

# Indica la forma del arreglo
arr.shape
```

### Reshape

```python
# transforma el arreglo mientras se mantengan los elementos.
arr.reshape(1,6) # [[4, 2, 4, 8, 4, 3]]
arr.reshape(2,3)
# [[4, 2, 4],
#  [8, 4, 3]]

np.reshape(arr,(1,6)) # [[4, 2, 4, 8, 4, 3]]

# Se puede hacer un reshape como lo haría C.
np.reshape(arr,(2,3), 'C')
# [[4, 2, 4],
#  [8, 4, 3]]

# Se puede hacer un reshape como lo haría Fortran.
np.reshape(arr,(2,3), 'F')
# [[4, 4, 8],
#  [4, 2, 3]]

#Además, existe la opción de hacer reshape según como esté optimizado nuestro computador.
np.reshape(arr,(2,3), 'A')
```