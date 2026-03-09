# ☁️ Data Lake para Análisis de Energía Renovable

![AWS](https://img.shields.io/badge/AWS-Data%20Lake-orange)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-purple)
![ETLT](https://img.shields.io/badge/Pipeline-ETLT-green)
![Status](https://img.shields.io/badge/Project-Data%20Engineering-blue)

---

# 📌 Descripción del Proyecto

Este proyecto implementa el diseño de una **arquitectura de Data Lake en la nube** para analizar el potencial de **energía renovable (solar y eólica)** utilizando datos meteorológicos históricos.

El objetivo es construir un **pipeline ETLT escalable** capaz de:

- Ingerir datos meteorológicos
- Almacenarlos en un Data Lake estructurado
- Transformarlos para análisis energético
- Permitir consultas analíticas y visualización

Las ubicaciones analizadas son:

- **Riohacha, Colombia** (alto potencial solar)
- **Patagonia, Argentina** (alto potencial eólico)

---

# 🎯 Objetivos

- Diseñar una arquitectura moderna de **Data Lake**
- Implementar un **pipeline ETLT**
- Analizar patrones meteorológicos
- Estimar **potencial energético renovable**
- Responder preguntas de negocio estratégicas

---

# ❓ Preguntas de Negocio

El sistema permitirá responder:

1. ¿Cómo varía el potencial solar durante el día y el mes en Riohacha y Patagonia?

2. ¿Qué patrones históricos existen en el potencial eólico?

3. ¿Qué condiciones climáticas reducen el potencial renovable?

4. ¿Cómo se comparan predicciones meteorológicas con datos históricos?

5. ¿Cuáles fueron los días con mayor y menor potencial energético?

---

# 🧱 Arquitectura del Data Lake

El Data Lake se organiza en **tres capas principales**.

## RAW Layer

Datos crudos sin transformación.



Características:

- Datos originales
- Formato JSON
- Fuente de verdad del sistema

---

## SILVER Layer (Processed)

Datos transformados y limpiados.

Procesos aplicados:

- limpieza de datos
- normalización de variables
- cálculo de métricas energéticas



---

## GOLD Layer (Analytics)

Datos optimizados para análisis y BI.



---

# 🔄 Arquitectura del Pipeline ETLT



El pipeline realiza:

1️⃣ Extracción de datos meteorológicos  
2️⃣ Carga al Data Lake  
3️⃣ Transformación de datos  
4️⃣ Análisis energético  

---

# ☁️ Arquitectura del Sistema

```mermaid
flowchart LR

A[Datos Meteorológicos JSON] --> B[Python Pipeline]
B --> C[RAW Layer - AWS S3]

C --> D[Transformación de Datos]
D --> E[Processed Layer - S3]

E --> F[AWS Glue Data Catalog]
F --> G[Consultas con Athena]

G --> H[Power BI / Dashboards]


| Tecnología         | Uso                       |
| ------------------ | ------------------------- |
| Python             | Procesamiento de datos    |
| Pandas             | Transformación y análisis |
| AWS S3             | Data Lake                 |
| AWS Glue           | ETL y catalogación        |
| AWS Lake Formation | Gobernanza de datos       |
| Amazon Athena      | Consultas SQL             |
| Power BI           | Visualización             |


📊 Variables Analizadas

Los datasets contienen variables meteorológicas como:

temperatura

humedad

velocidad del viento

nubosidad

precipitación

presión atmosférica

índice UV

Estas variables permiten calcular:

potencial solar estimado

potencial eólico estimado

📁 Estructura del Proyecto
energia-renovable-data-lake/

data/
    Riohacha_11_538415.json
    Patagonia_-41.json

scripts/
    pipeline_energia_renovable.py

output/
    energia_procesada.csv

README.md
📈 Resultados del Pipeline

El pipeline procesa aproximadamente:

17,568 registros meteorológicos

Resultados obtenidos:

cálculo de potencial solar

análisis de patrones de viento

correlación entre clima y generación energética

identificación de días con mayor producción energética

🔐 Gobernanza de Datos

La gobernanza del Data Lake se gestiona mediante:

control de accesos

catalogación de datos

políticas de seguridad

Esto se implementa utilizando AWS Lake Formation.

🚀 Conclusión

El diseño del Data Lake permite construir una arquitectura escalable, gobernada y preparada para análisis avanzado.

Este pipeline establece la base para futuras fases del proyecto, incluyendo:

modelos predictivos de generación energética

dashboards interactivos

análisis comparativos entre regiones.


