# Parámetros más usados con Seaborn

Seaborn tiene una gran variedad de gráficos, pero también tiene **ciertos parámetros**
 para cada gráfico, vamos a ver cuáles son los más comunes:

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Usar un dataset precargado de Seaborn
tips = sns.load_dataset('tips')

# Seaborn está adaptado para soportar dataframes
sns.displot(data=tips, x="total_bill")
plt.show()

# Agregamos una variable ‘Y’, pero seaborn reconoce que en gráfico de 
# frecuencias no es la mejor opción y lo adapta automáticamente
sns.displot(data=tips, x="total_bill", y="tip")
plt.show()

# Hacer agrupamiento por una variable hue
sns.displot(data=tips, x="total_bill", y="tip",hue="sex")
plt.show()

# Cambiar el tipo de gráfica kind
sns.displot(data=tips, x="total_bill",hue="sex",kind="kde")
plt.show()

# Quitar la leyenda
sns.displot(data=tips, x="total_bill",hue="sex",kind="kde", legend=False)
plt.show()

# Cambiar la paleta y su transparencia
sns.displot(data=tips, x="total_bill",hue="sex",kind="kde", legend=False, 
		palette="dark", alpha=.5)
plt.show()
```