# Set

Es un método de Seaborn que permite configurar el estilo, fuente y color de las gráficas.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Establecer estilo, paleta de color, fuente y tamaño de la fuente de las gráficas
sns.set(style="darkgrid",palette="muted",font="verdana",font_scale=2)
# Genera un gráfico de barras
sns.barplot(x=["A","B","Y","C"],y=[1,2,3,4])
# Seaborn trabaja sobre matplotlib
plt.show()
```

*Datos Importantes*

*Este método afecta a todas las gráficas que creamos, incluidas las que no usan Seaborn.*

*Podemos resetear los valores utilizando el método reset_orig.*

*Este método es un atajo de set_theme, que es el recomendado según la documentación*