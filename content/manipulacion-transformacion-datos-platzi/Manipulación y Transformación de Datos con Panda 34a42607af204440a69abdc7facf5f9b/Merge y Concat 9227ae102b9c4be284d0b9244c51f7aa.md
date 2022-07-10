# Merge y Concat

## Concat

```python
import pandas as pd
import numpy as np

# Crear dos nuevos dataframe
data = {"A":["A0","A1","A2","A3"],
        "B":["B0","B1","B2","B3"],
        "C":["C0","C1","C2","C3"],
        "D":["D0","D1","D2","D3"]}
df = pd.DataFrame(data)

data2 = {"A":["A4","A5","A6","A7"],
        "B":["B4","B5","B6","B7"],
        "C":["C4","C5","C6","C7"],
        "D":["D4","D5","D6","D7"]}
df2 = pd.DataFrame(data2)

# Concatenar ambos dataframes
pd.concat([df1,df2])

# Corregir los índices
pd.concat([df1,df2], ignore_index= True)

# Concatenar a nivel de columnas
pd.concat([df1,df2], axis = 1)
```

## Merge

```python
left = pd.DataFrame({"key":["k0","k1","k2","k3"],
 "A": ["A0","A1","A2","A3"],
 "B": ["B0","B1","B2","B3"]})

right = pd.DataFrame({"key":["k0","k1","k2","k3"],
 "C": ["C0","C1","C2","C3"],
 "D": ["D0","D1","D2","D3"]})

# Unir right a left
left.merge(right)

left = pd.DataFrame({"key":["k0","k1","k2","k3"],
 "A": ["A0","A1","A2","A3"],
 "B": ["B0","B1","B2","B3"]})

right = pd.DataFrame({"key_2":["k0","k1","k2","k3"],
 "C": ["C0","C1","C2","C3"],
 "D": ["D0","D1","D2","D3"]})

# Hay diferencias entre algunas columnas, por esa razón 
# hay que separarlos de esta manera:
left.merge(right,left_on="key",right_on="key_2")

left = pd.DataFrame({"key":["k0","k1","k2","k3"],
 "A": ["A0","A1","A2","A3"],
 "B": ["B0","B1","B2","B3"]})

right = pd.DataFrame({"key_2":["k0","k1","k2",np.nan],
 "C": ["C0","C1","C2","C3"],
 "D": ["D0","D1","D2","D3"]})

# Si tenemos un NaNen nuestro DataFrame, 
# pandas no lo detectará como un mach. Se soluciona con How, 
# dando así, una preferencia.
left.merge(right,left_on="key",right_on="key_2",how="left")
```