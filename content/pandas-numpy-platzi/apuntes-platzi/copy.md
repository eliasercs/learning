# Copy

`.copy()`nos permite copiar un array de NumPy en otra variable de tal forma que al modificar el nuevo array los cambios no se vean reflejados en array original.

```python
import numpy as np

arr = np.arange(0, 11) # [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10]

# Tomamos un trozo del array original
trozo_arr = arr[0:6] # [0, 1, 2, 3, 4, 5]

# Queremos pasar todas nuestros elementos a 0
trozo_de_arr[:] = 0 # [0, 0, 0, 0, 0, 0]

# Se han modificado los datos del array original porque 
# seguía haciendo referencia a esa variable.
print(arr) # [ 0,  0,  0,  0,  0,  0,  6,  7,  8,  9, 10]

# Con .copy() creamos una copia para no dañar nuestro array original
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy) #array([100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100])
print(arr) #array([ 0,  0,  0,  0,  0,  0,  6,  7,  8,  9, 10])
```

Esta función te ayudará a prevenir muchos errores y tener más confianza a la hora de manipular los datos