# Colores y estilos

Podemos personalizar mejor nuestros gráficos con diferentes colores y estilos, así, se entenderá mucho mejor nuestras gráficas.

```python
import matplotlib.pyplot as plt
import numpy as np

print(plt.style.available) # Estilos disponibles

plt.style.use("ggplot") # Aplicar un estilo

fig, axes = plt.subplots(figsize=(8,8))
axes.plot(x,x+1,color="red", alpha=0.5)
axes.plot(x,x+2,color="#000000", linewidth=1)
axes.plot(x,x+3,color="blue", linestyle="--", marker="o", markersize=18, 
		markerfacecolor="green")
```