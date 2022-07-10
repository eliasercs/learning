# Creando Arrays

Numpy nos da varios métodos muy eficientes para poder crear arrays desde 0.

```python
import numpy as np

# Este método de NumPy nos permite generar arrays sin definir previamente una lista.
np.arange(0,10)

# Un tercer argumento permite definir un tamaño de paso.
np.arange(0,20,2)

# np.zeros() Nos permite definir estructuras o esquemas.
np.zeros(3) # array([0., 0., 0.])

# De igual manera, tenemos np.ones()
np.ones(3) # array([1., 1., 1.])

# np.linspace() Permite generar una array definiendo un inicio, 
# un final y cuantas divisiones tendrá.
np.linspace(0, 10 , 10)

# También podemos crear una matriz con una diagonal de 1 y el resto de 0
np.eye(4)

# Otro método importante es generar números aleatorios.
np.random.rand()

# También se pueden generar vectores.
np.random.rand(4)

# Y a su vez generar matrices.
np.random.rand(4,4)

# NumPy nos permite también generar números enteros.
# En este caso números enteros entre el 1 y 14
np.random.randint(1,15)

# También podemos llevarlos a una estructura definida.
np.random.randint(1,15, (3,3))
```