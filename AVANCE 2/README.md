🚀 Segundo Avance – Proyecto Integrador
Ingesta de Datos con Airbyte

Bootcamp: Data Engineering – Henry
Estudiante: Luis Ramón Buruato
Módulo: M4
Componente: Data Ingestion Pipeline

📌 Contexto del Proyecto

Con la arquitectura del sistema previamente definida, el objetivo de este avance es implementar el componente de ingesta de datos del pipeline.

Para ello se utilizó Airbyte Cloud (Free Tier) como herramienta de integración de datos, permitiendo extraer información desde múltiples fuentes y cargarla dentro de la capa raw del Data Lake en Amazon S3.

Este proceso establece el flujo inicial de datos dentro del sistema y garantiza:

conectividad entre fuentes y destino

consistencia de los datos

trazabilidad del proceso de ingestión

escalabilidad para transformaciones posteriores

La arquitectura implementada sigue el modelo ELT (Extract, Load, Transform).

🏗️ Arquitectura del Pipeline

El flujo de datos implementado es el siguiente:

What is this?
⚙️ Configuración de Airbyte Cloud

Se utilizó Airbyte Cloud Free Tier para configurar los pipelines de ingesta.

Dentro de Airbyte se configuraron los siguientes componentes:

Sources

1️⃣ API pública (OpenWeatherMap)
2️⃣ Base de datos PostgreSQL pública

Destination

Amazon S3 Bucket

Capa raw/ del Data Lake

Conexiones

Se configuraron connections en Airbyte para sincronizar los datos desde las fuentes hacia el destino S3.

Debido a las limitaciones del Free Tier, las sincronizaciones se ejecutan manualmente una vez por día.

🌐 Conector de API Pública

Para la extracción de datos desde una API pública se utilizó el HTTP Connector de Airbyte.

API utilizada:

https://openweathermap.org/api

Autenticación realizada mediante API Key generada en:

https://home.openweathermap.org/api_keys

Configuración del conector
Parámetro	Configuración
Método HTTP	GET
Formato de respuesta	JSON
Autenticación	API Key
Endpoint	OpenWeatherMap
Datos extraídos

Los datos obtenidos corresponden a información meteorológica de diferentes ubicaciones.

Archivos generados:

Patagonia_-41.json
Riohacha_11_538415.json

Estos archivos contienen variables meteorológicas como:

temperatura

humedad

presión atmosférica

velocidad del viento

condiciones climáticas

🗄️ Conector de Base de Datos PostgreSQL

La segunda fuente de datos utilizada fue una base de datos PostgreSQL pública.

Para ello se utilizó el conector nativo de PostgreSQL en Airbyte.

Configuración de conexión
Parámetro	Descripción
Host	servidor PostgreSQL
Puerto	5432
Database	base pública
Usuario	credenciales de solo lectura
Password	credenciales seguras

Las credenciales utilizadas tienen permisos read-only, garantizando seguridad en la conexión.

🔄 Estrategia de Sincronización

Se implementaron dos tipos de sincronización:

Primera ejecución

Full Refresh

Carga completa de la tabla desde PostgreSQL hacia el Data Lake.

Sincronizaciones posteriores

Incremental Sync

Solo se cargan registros nuevos o modificados, optimizando el uso de recursos.

☁️ Destino de Datos – Amazon S3

Los datos extraídos son almacenados en un bucket de Amazon S3, que funciona como Data Lake del proyecto.

Configuración utilizada:

Parámetro	Configuración
Destino	Amazon S3
Bucket	Data Lake
Capa	raw/
Formato	Parquet


🗂️ Estructura del Data Lake

Los datos se almacenan dentro de la capa raw, manteniendo la información sin transformaciones.

Ejemplo de estructura:

data-lake
│
└── raw
    │
    ├── api_data
    │   ├── Patagonia_-41.json
    │   └── Riohacha_11_538415.json
    │
    └── postgresql_data
        └── tables.parquet

Esta estructura permite:

trazabilidad de los datos

auditoría del pipeline

procesamiento posterior en capas transformadas



✅ Validación de la Ingesta

Después de ejecutar las sincronizaciones en Airbyte se validó que los datos fueran almacenados correctamente en S3.

Se verificó:

✔ existencia de archivos en el bucket

✔ estructura correcta del Data Lake

✔ formato de almacenamiento Parquet

✔ correspondencia con los datos de las fuentes

Las pruebas confirmaron que la ingestión se ejecutó correctamente.

📸 Evidencias

Evidencias de la implementación del pipeline:

Airbyte Source

Configuración del conector HTTP hacia la API.

Source:

https://cloud.airbyte.com/workspaces/71b2d199-c217-4aec-8c44-0f5ba91ce4f1/source

Screenshot:

### Airbyte Source

![Airbyte Source](docs/airbyte_source.png)

### Airbyte Connection

![Airbyte Connection](docs/airbyte_connection.png)

### Amazon S3 Raw Layer

![S3 Raw Layer](docs/s3_raw_layer.png)



📁 Estructura del Proyecto
AVANCE_2
│
├── README.md
│
├── data
│   └── raw
│       ├── Patagonia_-41.json
│       └── Riohacha_11_538415.json
│
└── docs
    ├── airbyte_source.png
    ├── airbyte_connection.png
    └── s3_raw_layer.png



🎯 Conclusión

La implementación de Airbyte permitió construir una capa de ingestión de datos escalable dentro de la arquitectura del proyecto.

Se logró integrar múltiples fuentes de datos y almacenarlas dentro de un Data Lake basado en Amazon S3, utilizando el formato Parquet para optimizar el procesamiento analítico.

Este avance establece la base para las siguientes etapas del pipeline:

transformación de datos

modelado analítico

visualización y dashboards

👨‍💻 Autor

Luis Ramón Buruato
Data Engineering Student – Henry




