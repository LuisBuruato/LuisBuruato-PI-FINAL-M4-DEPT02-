# Proyecto Integrador – Data Engineering M4

Este repositorio contiene el desarrollo del **Proyecto Integrador del Módulo 4 (Data Engineering)**.
El proyecto implementa un **pipeline de datos completo**, desde la ingesta hasta la orquestación y automatización del flujo de datos.

---

# Estructura del repositorio

El proyecto está organizado en diferentes **avances del módulo**, distribuidos en dos ramas del repositorio.

## Rama `master`

La rama **master** contiene los avances iniciales del proyecto:

### AVANCE 1

* Definición de la arquitectura del Data Pipeline.
* Diseño del Data Lake.
* Selección de tecnologías para ingesta, almacenamiento y procesamiento.

### AVANCE 2

* Implementación de la capa de **ingesta de datos**.
* Integración con APIs o fuentes externas.
* Almacenamiento inicial en la capa **Raw** del Data Lake.

### AVANCE 3

* Implementación de procesos de **transformación de datos**.
* Uso de herramientas de procesamiento como Spark o scripts de transformación.
* Generación de capas intermedias del Data Lake (Bronze / Silver).

---

## Rama `main`

La rama **main** contiene el **AVANCE 4**, donde se completa la automatización del pipeline.

### AVANCE 4 – Orquestación y CI/CD

En esta etapa se implementa:

* Orquestación del pipeline con **Apache Airflow**
* Despliegue del entorno en **AWS EC2**
* Automatización del flujo de datos mediante DAGs
* Manejo de dependencias y ejecución de tareas del pipeline
* Integración de **CI/CD con GitHub Actions**
* Validación automática del pipeline al realizar cambios en el repositorio

El pipeline ejecuta las siguientes etapas:

1. Ingesta de datos
2. Transformación de datos
3. Carga a la capa **Gold** del Data Lake en formato **Parquet**

---

# Tecnologías utilizadas

* Python
* Apache Airflow
* Apache Spark
* Docker
* AWS EC2
* Git y GitHub
* GitHub Actions
* Parquet

---

# Objetivo del proyecto

Construir un **pipeline de datos automatizado, escalable y mantenible**, capaz de:

* Ingerir datos desde distintas fuentes
* Transformarlos mediante procesos ETL
* Orquestar el flujo completo con Airflow
* Implementar integración continua (CI/CD)
* Mantener control de versiones mediante Git

---

# Autor

Luis Buruato
Proyecto Integrador – Data Engineering
