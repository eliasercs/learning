# Operaciones

**Existen diferentes operaciones** que se pueden usar para los arrays de NumPy.

```python
import numpy as np

lista = [1,2]
# Una lista de Python entiende que quieres duplicar los datos. No es lo que buscamos.
lista * 2 # [1, 2, 1, 2]

# Pero Numpy lo entiende mucho mejor
arr = np.arange(0,10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = arr.copy() # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr * 2 # array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])
# Operación suma de vectores:
arr + 2 # array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

# División con un vector
# Como en este caso la primera posición del array es 0, 
# muestra un error pero, no detiene el proceso.
1 / arr2
# RuntimeWarning: divide by zero encountered in true_divide
#  """Entry point for launching an IPython kernel.
# array([    inf,   1.  , 0.5 , 0.33333333, 0.25 ,0.2, 0.16666667, 
# 0.14285714, 0.125 , 0.11111111])
```