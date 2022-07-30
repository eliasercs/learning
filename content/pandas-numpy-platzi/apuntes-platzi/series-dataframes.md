# Series y DataFrames en Pandas

Pandas es una librería de Python especializada en el **manejo y análisis de estructuras de datos**. El nombre viene de “Panel data”.

- Velocidad
- Poco código
- Múltiples formatos de archivos
- Alineación inteligente

### Pandas Series

Es muy parecido a un array de una dimensión ***(o vector)*** de NumPy.

- Arreglo unidimensional indexado
- Búsqueda por índice
- Slicing
- Operaciones aritméticas
- Distintos tipos de datos

### Pandas DataFrame

Muy parecido a las estructuras ***matriciales*** trabajadas con NumPy.

- Estructura principal
- Arreglo de dos dimensiones
- Búsqueda por índice (columnas o filas)
- Slicing
- Operaciones aritméticas
- Distintos tipos de datos
- Tamaño variable

### Series

Es un arreglo ***unidimensional*** indexado

```python
import pandas as pd

# Definiendo una lista con ***índices específicos***
players = pd.Series(["aodhaoidh","shaiodgsa","sahioahid","hdiohsaoh"],
          index=[1,7,6,5])

data = {1: "aodhaoidh",7: "shaiodgsa", 6: "sahioahid", 5: "hdiohsaoh"}
pd.Series(data)

# Búsqueda por ***índices***
players[1]

# Búsqueda mediante Slicing
players[0:3]
```

### Pandas

Similar a la estructura matricial

```python
import pandas as pd

data_players = {"jugador": ["aodhaoidh","shaiodgsa","sahioahid","hdiohsaoh"],
								"altura":[1,2,3,4]}
df_players = pd.DataFrame(data_players,index=[1,7,6,5])

# Búsqueda por índices. Columnas
df_players.columns

#Búsqueda por índice.
df_players.index
```