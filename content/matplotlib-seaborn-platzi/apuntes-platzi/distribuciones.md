# Distribuciones

Qué graficas u opciones permiten trabajar con distribuciones orientadas a tipos de datos numéricos

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Gráfico para distribuciones y que se acumulen cumulative
sns.histplot(data=tips, x="tip", bins=15,cumulative=True)
plt.show()

# Como muestra en el eje y stat, presentar los datos multiple
sns.histplot(data=tips, x="tip", bins=15,cumulative=False,hue="sex", stat="percent",multiple="dodge")
plt.show()

sns.kdeplot(data=tips,x="tip",hue="sex",shade=True,bw_adjust=1)

# Proporción
sns.ecdfplot(data=tips,x="tip",hue="sex")

sns.displot(data=tips,x="tip",hue="sex",kind="kde", multiple="stack")
```