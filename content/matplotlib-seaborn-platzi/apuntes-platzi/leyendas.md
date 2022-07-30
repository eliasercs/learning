# Leyendas, títulos, etiquetas, tamaño

Para dar **contexto** a nuestros gráficos necesitamos usar títulos, leyendas, tamaño o etiquetas, para que nuestra gráfica tenga un contexto más amplio.

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(5,5))
axes[0].plot(x,y,label="$sin(x)$")
axes[0].set_title("Relación X - Y")
axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[0].legend(loc="lower left")
axes[1].plot(y,x)
axes[1].set_title("Relación Y - X")
axes[1].set_xlabel("Y")
axes[1].set_ylabel("X")

fig.tight_layout()
```