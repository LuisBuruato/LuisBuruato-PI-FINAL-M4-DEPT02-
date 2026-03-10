📘 README — AVANCE 1

AVANCE 1 – Diseño de Arquitectura del Pipeline
Descripción

En este primer avance se plantea el diseño de la arquitectura del pipeline de datos que será desarrollado durante el proyecto integrador.

El objetivo principal es definir cómo fluirán los datos desde las fuentes originales hasta las capas finales de análisis dentro de un Data Lake.

Objetivos del avance

Definir la arquitectura general del pipeline de datos.

Diseñar la estructura del Data Lake.

Identificar las herramientas y tecnologías a utilizar.

Establecer el flujo de procesamiento de datos.

Arquitectura del pipeline

El flujo de datos propuesto sigue las siguientes etapas:

Fuente de datos
↓
Proceso de ingesta
↓
Data Lake (Raw Layer)
↓
Procesamiento y transformación
↓
Data Lake (Silver / Gold)
↓
Consumo analítico

Tecnologías consideradas

Durante el diseño se seleccionaron las siguientes herramientas:

Python

Apache Spark

Apache Airflow

Docker

AWS Cloud Services

Git y GitHub

Resultado del avance

Se definió la arquitectura base del sistema de datos, que servirá como guía para la implementación de los siguientes avances del proyecto.

📘 README — AVANCE 2
Writing
AVANCE 2 – Implementación de Ingesta de Datos
Descripción

En este avance se desarrolla el proceso de ingesta de datos, que permite obtener información desde fuentes externas y almacenarla en la capa inicial del Data Lake.

El objetivo es construir un mecanismo que permita capturar datos de forma estructurada para su posterior procesamiento.

Objetivos del avance

Implementar scripts de extracción de datos.

Conectar con fuentes de datos externas (APIs o datasets).

Almacenar los datos en la capa Raw del Data Lake.

Garantizar que los datos estén disponibles para procesos de transformación posteriores.

Flujo de ingesta

El proceso de ingesta sigue el siguiente flujo:

Fuente de datos
↓
Script de extracción
↓
Validación básica
↓
Carga al Data Lake (Raw)

Tecnologías utilizadas

Para implementar esta etapa se utilizaron:

Python

APIs públicas

Scripts de extracción de datos

Almacenamiento estructurado de archivos

Resultado del avance

Se implementó un sistema inicial de ingesta de datos, permitiendo capturar información desde las fuentes y almacenarla correctamente dentro del Data Lake.

📘 README — AVANCE 3
Writing
AVANCE 3 – Transformación y Procesamiento de Datos
Descripción

En este avance se implementa la etapa de transformación de datos, donde los datos almacenados en la capa Raw son procesados para generar información estructurada y lista para análisis.

El objetivo es limpiar, transformar y estructurar los datos para generar datasets de mayor calidad.

Objetivos del avance

Procesar los datos provenientes de la capa Raw.

Realizar procesos de limpieza y normalización de datos.

Generar datasets estructurados.

Preparar la información para su consumo analítico.

Flujo de transformación

El procesamiento de datos sigue el siguiente flujo:

Datos Raw
↓
Limpieza de datos
↓
Transformación de estructuras
↓
Optimización del formato
↓
Almacenamiento en capas superiores del Data Lake

Tecnologías utilizadas

Para esta etapa se emplearon las siguientes herramientas:

Python

Apache Spark

Procesamiento de datos distribuido

Formato de almacenamiento optimizado Parquet

Resultado del avance

Se generaron datasets transformados y estructurados, listos para ser utilizados en procesos analíticos o sistemas de visualización.
