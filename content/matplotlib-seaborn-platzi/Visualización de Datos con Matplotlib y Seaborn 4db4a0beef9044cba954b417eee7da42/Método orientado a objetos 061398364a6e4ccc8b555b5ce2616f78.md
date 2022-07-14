# Método orientado a objetos

Hay **distintas maneras** de hacer gráficas dentro de Matplotlib, ya vimos pyplot; sin embargo, es muy complicado personalizarla y entrar a ciertos parámetros.

### Método orientado a objetos

Un objeto define una figura, esa figura es un lienzo en el cual podemos introducir diferentes grá ficas(axes), de las cuales cada una posee sus propios ejes(axis).

La figura representa el todo, dentro de ella vamos a configurar gráficas las cuales contienen diferentes ejes.

Es un poco **más complicado**, pero en el mismo gráfico podemos personalizarlo mucho mejor.

![https://static.platzi.com/media/user_upload/Captura-845012cb-41c1-4c4b-bad5-427afbf00703.jpg](https://static.platzi.com/media/user_upload/Captura-845012cb-41c1-4c4b-bad5-427afbf00703.jpg)

Pyplot

- Rápido
- Fácil
- Una sola figura

Object Oriented

- Mayor personalización
- Más código
- Más amigable a múltiples diagramas

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x**2

# Utilizar el concepto de objeto
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.5,0.9]) # pos x, pos y, width, height
axes.plot(x,y)

# Personalización
fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes.plot(x,y,"b")
axes2.plot(y,x,"r")
fig.show()
```