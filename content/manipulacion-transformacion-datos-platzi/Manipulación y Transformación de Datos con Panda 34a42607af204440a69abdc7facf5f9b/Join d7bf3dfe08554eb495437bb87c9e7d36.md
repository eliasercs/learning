# Join

`Join`Es otra herramienta para hacer exactamente lo mismo, una combinación. La diferencia es que **join va a ir a los índices y no a columnas específicas.**

```python
left = pd.DataFrame({'A': ['A0','A1','A2'],
  'B':['B0','B1','B2']},
  index=['k0','k1','k2'])

right = pd.DataFrame({'C': ['C0','C1','C2'],
  'D':['D0','D1','D2']},
  index=['k0','k2','k3'])

# Combinar izquierda con derecha
left.join(right)

# Traer todos los datos aunque no exista relación
left.join(right, how='outer')

# Traer todos los datos que tengan relación
left.join(right,how='inner')

# Traer los datos relacionados incluyendo a los 
# no relacionados del dataframe izquierdo
left.join(right,how='left')

# Traer los datos relacionados incluyendo a los 
# no relacionados del dataframe derecho
left.join(right,how='right')
```