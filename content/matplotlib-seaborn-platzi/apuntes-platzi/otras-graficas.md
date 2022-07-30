# Crear otro tipo de gráficas

Existen otros tipos de gráficos que Matplotlib nos proporciona para ser mucho **más certeros en nuestros análisis.**

```python
import matplotlib.pyplot as plt
import numpy as np

plt.hist(data,bins=10,width=2,histtype="bar")
plt.show()

plt.hist(data,histtype="step")
plt.show()

plt.boxplot(data,vert=False, patch_artist=True, notch=True)
plt.show()

n = 50
x = np.random.rand(n)
y = np.random.rand(n)
area = (30* np.random.rand(n)) **2
colors = np.random.rand(n)

plt.scatter(x,y,s=area,c=colors,marker="^",alpha=0.5)
plt.show()
```