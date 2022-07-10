# Condiciones

Las condiciones nos permiten ***hacer consultas más específicas.***

```python
import np as numpy

arr = np.linspace(1,10,10, dtype = 'int8') 
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10], dtype=int8)

# Regresa un array de booleanos dónde la condición se cumple.
indices_cond = arr > 5 
#[False, False, False, False, False,  True,  True,  True,  True, True]

# Regresa los valores para dónde la condiciones True.
arr[indices_cond]

# Múltiples condiciones.
arr[(arr > 5) & (arr < 9)]

# Modificar los valores que cumplan la condición.
arr[arr > 5] = 99
```