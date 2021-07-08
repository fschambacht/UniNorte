# UniNorte
Studies in programming skills (Python) at the Universidad del Norte Colombia

# Reto habilidades de programacion-Python UNINORTE
### (Estudio de condiciones para plantaciones de cacao)
En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Para el 2030, se busca luchar contra la desertificación, rehabilitar las tierras y los suelos degradados, incluidas de las tierras afectadas por la desertificación, la sequía y las inundaciones, y procurar lograr un mundo con una degradación neutra del suelo.

El Ministerio de Agricultura y Desarrollo Rural busca recuperar los suelos para el cultivo del cacao. Para poder cumplir con esto han iniciado el análisis los nutrientes disponibles en el suelo donde se tiene previsto iniciar las plantaciones. Para esta tarea lo requieren a usted y se facilita una tabla que describe si el entorno es apto o no.

|  CARACTERISTICAS | SUMAMENTE APTO | MODERADAMENTE APTO | MARGINALMENTE APTO  | NO APTO  |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  Acidez (pH) |  (5.5 - 6.5] |  (6.5 - 7.0] o [5.5 –5.0) | (7.0 - 8.0] o [5.0-4.5]  |  > 8.0 o < 4.5 |
|  Materia orgánica (% total) | > 5%  | (4 – 5]  | [3 – 4]  | < 3% |

Para esta nueva etapa del desarrollo se consolidaron las características del suelo de distintas zonas de las capitales del país. Estas se encuentran en un archivo llamado data.csv que cuenta con las siguientes columnas:

- Capital: nombre de la ciudad capital
- ID Zona: identificador de la zona, numerado de 0 – 3124 por cada ciudad
- Altura sobre el nivel del mar: el valor obtenido de la altura en esa zona
- Temperatura media anual: el valor obtenido de la temperatura en esa zona
- Precipitación anual: el valor obtenido de la precipitación en esa zona
- Profundidad efectiva del suelo: el valor obtenido de la profundidad en esa zona
- Aptitud: si la zona es sumamente, marginalmente, moderadamente o no apta

La aptitud se calculó analizando los valores para:

- Acidez
- Materia orgánica

Y se tuvo en cuenta el siguiente criterio para la conclusión:

-  Si ambas variables se encuentran dentro de la misma categoría se escogerá la categoría.
- Si están en categorías diferentes se escogerá la peor de ellas.

El estudiante deberá:

- Leer una ciudad

Y para esta ciudad deberá:

- Imprimir el promedio de las variables analizadas separadas por espacio, y formateadas a dos cifras decimales
- Imprimir el mínimo de ambas variables separadas por un espacio
- Imprimir el máximo de ambas variables separadas por un espacio
- Imprimir el conteo de cada categoría. Se deberán imprimir las categorías de mayor a menos conteo. Si se encuentran dos categorías con el mismo valor se imprimirán de manera alfabética ascendente
