# Cómo estructurar queries en SQL

**En esta clase vamos aprender a realizar queries en SQL a usarlos para ejemplos de empresas.**

Esto nos va ayudar a extraer información de una tabla, la información en la que estés interesado para un análisis posterior 

# Ejemplo de SQL

![Co%CC%81mo%20estructurar%20queries%20en%20SQL%20271f256731614ede8870268389bbf043/Como_estructurar_queries_en_SQL_en_Curso_de_Analisis_de_Negocios_para_Ciencia_de_Datos_.jpg](Co%CC%81mo%20estructurar%20queries%20en%20SQL%20271f256731614ede8870268389bbf043/Como_estructurar_queries_en_SQL_en_Curso_de_Analisis_de_Negocios_para_Ciencia_de_Datos_.jpg)

Ahora que ya hemos revisado la sintaxis de SQL vamos a ver cómo transformar esta sintaxis en un código que funcione, en un código útil para tu empresa 

Aquí tenemos un **OBJETIVO** que nos ha puesto esta empresa que vende bocinas. 

Quiere saber ¿Cuántas bocinas ha vendido por más de 600MXN desde 2019?

Y tenemos una tabla de excel (bbdd) con los registros de ventas (la información). Esta tabla se llama **VENTAS_2020**

Las diferentes columnas son DÍA, MES, AÑO, PRODUCTO y VALOR

 

```sql
SELECT COUNT (DISTINCT id)
FROM VENTAS_2020
WHERE Producto = "Bocina"
AND Valor > 600
AND Año >= 2019
```

<aside>
👨🏻‍💻 **RESULTADO = 2**

</aside>

### Para crear la tabla posteado por Leonardo Castro Barrantes

```sql
CREATE TABLE VENTAS_2020 (
	Dia int not null,
	Mes int not null, 
	Anio int not null,
	Producto varchar (25) not null,
	id int PRIMARY KEY,
	valor int not null
);

INSERT INTO VENTAS_2020 (Dia, Mes, Anio, Producto, id, valor)
values (1,2,1998,'Bocina',24,528),
	   (12,4,2004, 'Auriculares',31,240),
	   (14,8,2016,'Auriculares',14, 315),
	   (16,10,2019,'Bocina',200,1050),
	   (21,12,2020,'Bocina',304,680);
```