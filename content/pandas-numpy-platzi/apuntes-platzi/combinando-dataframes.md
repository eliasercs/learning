# Combinando DataFrames

Existen diferentes formas de fusionar dos DataFrames. Esto se hace a través de la **lógica de combinación** como se muestra a continuación:

![https://static.platzi.com/media/user_upload/merge-join-bce1f2e4-f1af-4fdd-8b80-a3d8926d9444.jpg](https://static.platzi.com/media/user_upload/merge-join-bce1f2e4-f1af-4fdd-8b80-a3d8926d9444.jpg)

- **Left join:** Da prioridad al DataFrame de la izquierda. Trae siempre los datos de la izquierda y las filas en común con el DataFrame de la derecha.
- **Right join:** Da prioridad al DataFrame de la derecha. Trae siempre los datos de la derecha y las filas en común con el DataFrame de la izquierda.
- **Inner join:** Trae solamente aquellos datos que son común en ambos DataFrame
- **Outer join:** Trae los datos tanto del DataFrame de la izquierda como el de la derecha, incluyendo los datos que comparten ambos.