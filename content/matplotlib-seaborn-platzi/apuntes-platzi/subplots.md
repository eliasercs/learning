# Subplots

Con subplots se puede trabajar en un **arreglo de gráficas** a las cuales se accede a través de los índices.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

# Generar varias gráficas dentro de un lienzo
fig, axes = plt.subplots(nrows=1,ncols=2)
# Generar cada gráfica
axes[0].plot(x,y,"b")
axes[1].plot(y,x,"y")

fig, axes = plt.subplots(nrows=2,ncols=3) # lienzo de 2 filas y 3 columnas
# Establecer cada gráfica
axes[0,0].plot(x,np.cos(x),"r")
axes[0,1].plot(x,np.sin(x),"g")
axes[0,2].plot(x,np.tan(x),"b")
axes[1,0].plot(x,np.cos(x)**2,"r")
axes[1,1].plot(x,np.sin(x)**2,"g")
axes[1,2].plot(x,np.tan(x)**2,"b")

fig.tight_layout() # Mejora la visualización de las figuras
```