# Leer archivos CSV y JSON

```python
import pandas as pd

# csv = normalmente son archivos separados por coma
pd.read_csv('Ruta del archivo')

# En algunas ocasiones el archivo podría estar separado por otro carácter, por lo que
# utilizamos el parámetro sep
pd.read_csv('Ruta del archivo', sep=',')

# Para especificar el número de filas a mostrar, utilizamos el parámetro header
pd.read_csv('Ruta del archivo', header=2)

# Para cambiar el nombre de las columnas, utilizamos el parámetro names
pd.read_csv('', header=0, names=[])

# Importar un archivo JSON
pd.read_json('Ruta del archivo')
```