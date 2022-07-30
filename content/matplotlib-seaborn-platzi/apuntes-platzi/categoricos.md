# Categóricos

Diferentes gráficos que ofrece Seaborn para graficar datos categóricos, variables de texto

```python
import seaborn as sns
import matplotlib.pyplot as plt

ticks = sns.load_dataset("ticks")

# Gráficos de cantidad
sns.countplot(data = tips, x= 'day', hue='sex')

# Diagrama de puntos
sns.swarmplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', dodge=True);

# Diagrama de caja
sns.boxplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', dodge=True);

# Se pueden combinar distintos gráficos
sns.boxplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', dodge=True);
sns.swarmplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', dodge=True, 
	color = '0', marker= '<');

# Violín: parecido a Boxplot, pero no muestra los cuartiles, sino como 
# se concentran los datos con comparación split
sns.violinplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', split=True);

# Catplot, con kind podemos cambiar el tipo de gráfico y 
# se puede agregar otra variable col
sns.catplot(data= tips, x= 'day', y = 'total_bill', hue= 'sex', dodge=True, 
	kind= 'box', col= 'time');
```