# Tipos de Datos

Los arrays de NumPy solo pueden contener un tipo de dato, ya que esto es lo que le confiere las ventajas de la ***optimización de memoria.***

```python
import numpy as np

arr = np.array([1, 2, 3, 4])

# Podemos conocer el tipo de datos del array consultando la propiedad .dtype
arr.dtype

# Si queremos usar otro tipo de dato, lo podemos definir en la declaración del array.
arr = np.array([1, 2, 3, 4], dtype = 'float64')

# Si ya se tiene el array definido, se utiliza el método .astype() para 
# convertir el tipo de dato.
arr = np.array([1, 2, 3, 4])
arr = arr.astype(np.float64)

# También se puede cambiar a tipo booleano recordando que los números 
# diferentes de 0 se convierten en True.
arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.bool_)

# También podemos convertir los datos en tipo string.
arr = np.array([0, 1, 2, 3, 4])
arr = arr.astype(np.string_)

# De igual manera, se puede pasar de string a número.
arr = np.array(['0', '1', '2', '3', '4'])
arr = arr.astype(np.int8)

# Si un elemento no es de tipo número, el método falla.
arr = np.array(['hola','0', '1', '2', '3', '4'])
arr = arr.astype(np.int8)
```

El array de Numpy únicamente puede tener un único tipo de datos en el cual va a trabajar. No puedo tener la mitad del array en ***int*** y la otra mitad en ***bool***
.