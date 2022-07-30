# Jointplot y Pairplot

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

# Joinplot = Une 2 gráficas distintas en una sola
sns.jointplot(data=tips, x='total_bill', y= 'tip', hue = 'sex')

# Ejemplo
sns.jointplot(data=tips, x='total_bill', y= 'tip', hue = 'sex',kind="hist", 
	marginal_ticks=True, marginal_kws=dict(bins=25, fill=False, multiple="dodge"))

# Pairplot = correlaciona toda la variable numérica que hay en el dataset
sns.pairplot(data= tips)

# Elimina información duplicada
sns.pairplot(data= tips, corner=True)
```