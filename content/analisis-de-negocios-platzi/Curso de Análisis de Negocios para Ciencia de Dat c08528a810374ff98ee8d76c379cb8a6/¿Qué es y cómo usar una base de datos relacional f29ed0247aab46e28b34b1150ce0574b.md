# ¿Qué es y cómo usar una base de datos relacionales con SQL?

![%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/Untitled.png](%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/Untitled.png)

En esta clase vas a convertirte en analista. 

**Bases de datos y funciones principales de SQL**

**ENTENDER LA SINTAXIS Y PRINCIPALES FUNCIONES DE SQL**

Aprendiendo SQL vas a poder extraer información, vas aprender mejor qué son las tablas, qué son las bases de datos.

Toda la información de la empresa queda almacenada  y eso se convierte en una tabla, la tabla tiene columnas y tiene filas. 

Las columnas pueden ser muy diversas, en este caso, hablamos de una tabla de ventas. Esta tabla contiene información de cuál es la orden, esto es un registro único de cada una de las ventas, tenemos información de la fecha en la que se realizó, cuál fue el importe por el que se compró este producto y quién compró este producto.     

![%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/icons8-static_view_level2.png](%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/icons8-static_view_level2.png)

![%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/Notification_Center.jpg](%C2%BFQue%CC%81%20es%20y%20co%CC%81mo%20usar%20una%20base%20de%20datos%20relacional%20f29ed0247aab46e28b34b1150ce0574b/Notification_Center.jpg)

Todos estos conjuntos de tablas de ventas, de clientes, de sucursales, etc. Conforman una base de datos. 

# EMPECEMOS CON SQL: INSTRUCCIONES DE COMANDOS SQL

**SQL** es la herramienta que nos va ayudar a sintetizar la información, a extraer datos de estas tablas. 

Lo primero que le tenemos que decir es, ¿dónde tenemos almacenada esta información? 

**COMANDOS: 
SELECT** selección de los campos (columnas) para hacer el análisis o para sintetizar la tabla de origen

Para decirle **SELECCIONAR**, es muy simple, es **SELECT** ahí le vas a decir, cuál es la columna que deseas seleccionar, por ejemplo: 

SELECT FECHA

SELECT CLIENTE 

Si en una misma consulta queremos seleccionado 2 o más, debemos separarlas por una coma (,)

SELECT Fecha, Cliente

*En tabla de código:* 

```sql
SELECT Fecha
SELECT Fecha, Cliente
```

[https://www.youtube.com/watch?v=gbHXhXmACgI](https://www.youtube.com/watch?v=gbHXhXmACgI)

**CLAUSULAS: 
FROM** Tabla donde se almacena la información
**WHERE** Especificar las condiciones
**GROUP BY** Campos (columnas) de agrupación
**ORDER BY** Campos (columnas) de ordenación

Lo siguiente será indicar dónde está almacenada esta información, para encontrar la información tienes que decirle **FROM** (from significa donde) y le vas a indicar el nombre de la tabla, en nuestro ejemplo, la tabla se llama ventas  

*En tabla de código:* 

```sql
FROM tabla donde se almacena la información
WHERE especificar las condiciones
GROUP BY columnas de agrupación
ORDER BY columnas de ordenación
```

Ejemplo: **EJEMPLO DE QUERY COMPLETO ¿QUÉ INFORMACIÓN QUIERES? ¿Y DÓNDE PUEDES ENCONTRARLA?**

```sql
SELECT Fecha, Cliente
FROM Ventas
```

Adicional a esto, puedes incluir muchas condiciones que te ayudarán a una mejor síntesis, una de estas funciones es el **WHERE** (where significa dónde) **y allí le vamos a poner una condición, por ejemplo, que sólo quieres las ventas del año 2020**

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Fecha = 2020
```

Otra condición es el **GROUP BY** (agrupar por) va servir para hacer una condición agrupada por una de las columnas, si solo quieres saber las ventas de los clientes, puedes indicar **GROUP BY** Cliente y te va indicar **cada cliente cuántas compras hizo, por qué valor, en qué fechas, también puedes agrupar por mes, para ver en este mes cuántas ventas se hicieron**

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Fecha = 2020
GROUP BY Cliente
```

El **ORDER BY** (ordenar por) nos sirve para ordenar los resultados, puedes ordenar tu estudio en función del mes, para tenerlo ordenado de Enero a Diciembre, o bien, también por año, o incluso, ordenarlo por el nombre del cliente (ascendente en orden alfabético).

 

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Fecha = 2020
GROUP BY Cliente
ORDER BY Mes
```

### FROM

[https://www.youtube.com/watch?v=MfI_wtO6OdI](https://www.youtube.com/watch?v=MfI_wtO6OdI)

### GROUP BY

[https://www.youtube.com/watch?v=Yvuw0dbd7OQ](https://www.youtube.com/watch?v=Yvuw0dbd7OQ)

### WHERE

[https://www.youtube.com/watch?v=4CdOYVZLJWE](https://www.youtube.com/watch?v=4CdOYVZLJWE)

### ORDER BY

[https://www.youtube.com/watch?v=6YGvqrwQ9d4](https://www.youtube.com/watch?v=6YGvqrwQ9d4)

**OPERADORES LÓGICOS: 
AND** Une varias condiciones que tienen que ser cumplidas para obtener resultados
**OR** Evalúa dos o más condiciones y obtienes resultados si una de ellas se cumple
**NOT** Excluye un valor de la información a obtener

Otras claúsulas son los **operadores lógicos,** estas instrucciones nos sirven para unir comandos, puedes indicar que te interesa saber que sean del año 2020 y que aparte las halla hecho una persona que se llama Ana.

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Fecha = 2020 
AND Cliente = ANA DOMÍNGUEZ
```

También puedes indicar que solo con que cumpla una sola de las condiciones ya te interesa obtener este resultado, esto se hace con la función **OR,** es una condición disyuntiva, solo con que se llame Ana, o con que la venta se halla hecho en el 2020 extrae esta información

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Fecha = 2020
OR Cliente = ANA DOMÍNGUEZ
```

También puedes usar la condicional **NOT** para decir NO INCLUYAS este tiempo de cliente NO  INCLUYAS este tipo de cliente 

```sql
SELECT Fecha, Cliente
FROM Ventas
WHERE Cliente = ANA DOMÍNGUEZ
NOT IN Fecha = 2020
```

**FUNCIONES AGREGADAS: 
AVG** Promedio (average) de un campo (columna)
**COUNT** Recuento de valores de una columna
**DISTINCT** Encontrar valores únicos
**SUM** Suma de valores de una columna
**MAX** Valor más alto de una columna
**MIN** Valor más bajo de una columna

Otras funciones muy útiles son las de **AGREGACIÓN** estas funciones nos ayudan a no tener que hacer estos cálculos de manera manual, por ejemplo, en el caso de que tengamos millones de registros. 

**Para hacer un promedio**

```sql
AVG con esta podríamos sacar el promedio de clientes que tuvimos el año pasado,
AVG el valor promedio de estas ventas 
AVG cuánto gastaron en promedio nuestros clientes 
AVG cuántas personas fueron 
```

**Para hacer recuentos y distinciones** 

```sql
COUNT cuántos clientes hubo
DISTINCT te llevas solamente aquellos usuarios únicos, no repetidos
```

**Si quieres sumar cuántas ventas se hicieron**

```sql
SUM sumar cuántas ventas se hicieron
SUM suma de todos los importes de determinado, mes día, etc 
```

Valores máximos

```sql
MAX cuál fue la persona que hizo una compra por el valor más elevado
```

Valores mínimos

```sql
MAX cuál fue la persona que hizo una compra por el menor valor
```