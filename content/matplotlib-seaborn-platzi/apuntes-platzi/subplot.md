# Subplot

Subplot permite crear gráficos dentro de una gráfica. Esto lo hace a través de una **matriz de gráficos** y se puede acceder a ellos a través de índices:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

# Los parámetros funcionan de subplot funcionan:
# Filas - Columnas - Índice
# Crear una matriz de gráficos de una fila y dos columnas
plt.subplot(1,2,1) # Grafico 1
plt.plot(x,y, 'r--') 

plt.subplot(1,2,2)  # Gráfico 2
plt.pie(y)
plt.show()

# Agregar diferentes Plot al gráfico
plt.subplot(1,2,1)
plt.plot(x,y, 'r--') # Plot 1
plt.plot(y,x, 'b:') #Plot 2

plt.subplot(1,2,2)
plt.pie(y)
plt.show()

# Invertir la matriz de los gráficos
plt.subplot(2,1,1) #Grafico 1
plt.plot(x,y,'r--') #Plot 1
plt.plot(y,x,'b:')  #Plot 2

plt.subplot(2,1,2) #Grafico 2
plt.pie(y)         #Plot 1  
plt.show()
```