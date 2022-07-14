# Relation

Gráficos de relación entre distintas variables numéricas que ofrece Seaborn para hacer visualizaciones

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# Establecer la relación entre la cuenta total y la propina
sns.scatterplot(data=tips,x="total_bill",y="tip")

# Segmenta por día
sns.scatterplot(data=tips,x="total_bill",y="tip", hue="day")

# Segmenta por almuerzo y cena
sns.scatterplot(data=tips,x="total_bill",y="tip", hue="day", style="time")

# Representar la cantidad de comensales
sns.scatterplot(data=tips,x="total_bill",y="tip",hue="day",style="time",size="size")

# Cambiar de posición la leyenda
plt.legend(loc="center",bbox_to_anchor=(1.12,0.5))

# Modificar los marcadores
markers = {"Lunch": "D", "Dinner": "s"}
sns.scatterplot(data=tips,x="total_bill",y="tip",hue="day",style="time",
		size="size",markers=markers)

# Ejemplo con gráfico de líneas
# Se recomienda utilizar con menos variables
sns.lineplot(data=tips,x="total_bill",y="tip",hue="day",style="time",size="size")
plt.legend(loc="center",bbox_to_anchor=(1.12,0.5))
plt.show()

# Separar la relación (almuerzo - cena) en dos columnas
sns.relplot(data=tips,x="total_bill",y="tip",hue="day",style="time",size="size",
		col="time")
plt.legend(loc="center",bbox_to_anchor=(1.12,0.5))
plt.show()
```