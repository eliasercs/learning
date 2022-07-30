# Pyplot básico

Pyplot es una herramienta que tiene Matplotlib para ejecutar gráficas de manera sencilla. Véamos cómo puedes lograrlo.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x**2

# Graficar en función de y
plt.plot(x,y)
# Muestra la gráfica
plt.show()

# Modificar el color de la gráfica
# "b" = blue, "g" = green, "m" = magenta
plt.plot(x,y,"m")

# Format strings o marcadores
# "." -> point marker
# "," -> pixel marker
# "o" -> circle marker
# "v" -> triangle down marker
# "^" -> triangle up marker
# "<" -> triangle left marker
# ">" -> triangle right marker
plt.plot(x,y,"go") # Gráfica de color verde con marcadores redondos

# Estilo de líneas
# "-" -> solid line style
# "--" -> dashed line style
# "-." -> dash-dot line style
# ":" -> dotted line style
plt.plot(x,y,"go:") # Gráfica de color verde con marcadores redondos y
# estilo de línea punteada

# Histógrama de los valores de x
plt.hist(x)

# Gráfica de pie
plt.pie(x)

# Conocer correlación entre variables
plt.scatter(x,y)

# Distribución de los datos (Gráfico de caja)
plt.boxplot(x)
```