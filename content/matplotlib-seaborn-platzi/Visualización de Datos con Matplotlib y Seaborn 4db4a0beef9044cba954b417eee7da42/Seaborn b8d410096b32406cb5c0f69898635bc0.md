# Seaborn

Seaborn es una librería construida sobre **Matplotlib,** por lo que hereda todas las bondades de la misma. Fue escrita por Michael Waskom y está integrada para **estructuras de Pandas** por lo que está optimizada para funcionar con DataFrames.

## Cuáles son las ventajas de Seaborn

Seaborn tiene diferentes ventajas y entre ellas encuentras principalmente:

- Tiene una gran velocidad
- Facilidad para escribir código
- Altamente customizable entre gráficas y visualizaciones

## Estructura básica

```python
sns.'Tipo de Grafica'(
		 data='Dataset',
		 x='Data en el eje x',
		 y='Data en el eje y',
		 hue='Variable de agrupamiento')
```

## Tipos de Gráficas que tiene Seaborn

Seaborn ofrece ciertas características principales para problemas específicos de visualización de datos:

- Diagramas o gráficas relacionables
- Distribución de datos
- Graficar variables categóricas

Por ejemplo:

- **Relplot (relacional):** scatterplot, lineplot.
- **Displot (distribuciones):** histplot, kdeplot, ecdfplot, rugplot.
- **Catplot (categorica):** stripplot, swamplot, boxplot, violinplot, pointplot, barplot.