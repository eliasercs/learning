# Heatmap

Heatmap es un tipo de gráfico enfocado a una estructura matricial. Correlaciona todas las variables numéricas del dataset

- -1 → Correlación totalmente indirecta
- 0 → No hay correlación
- 1 → Correlación directa

Los valores intermedios representan el tipo de correlación (negativa, neutra o positiva)

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Correlación entre variables
tips.corr()

# Heatmap
sns.heatmap(tips.corr())

# Se pueden agregar diferentes parámetros. annot muestra el valor de la correlación,
# cmap color,linewidthsespacio entre variables, linecolor color de las líneas, vm
# inv, max valores máximos y mínimos, cbar=False eliminar la barra
```