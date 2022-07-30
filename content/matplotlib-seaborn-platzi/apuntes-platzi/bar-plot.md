# Bar plot

El gráfico de barras nos permite graficar variables categóricas, es decir, variables de texto, lo que es muy importante en el mundo de la ciencia de datos y Matplotlib ofrece ciertas características que nos facilita la vida en cuanto a graficar este tipo de variables.

```python
import matplotlib.pyplot as plt
import numpy as np

country = ["Chile","Argentina","México","Colombia","Japón"]
population = [12000,23000,40000,10000,50000]

plt.bar(country,population,width=0.5, color=["red","green"])
plt.xticks(np.arange(len(country)),["Chile","Argentina","México","Colombia","Japón"]
	,rotation=90)
```