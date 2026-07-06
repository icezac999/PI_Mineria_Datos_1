# PI_Mineria_Datos_1

## Información general
Proyecto Integrador de la materia Minería de Datos 1. Trabajo grupal sobre un dataset de usuarios de una plataforma de streaming, con el objetivo de aplicar un proceso completo de análisis de datos: inspección, limpieza, EDA, reducción de dimensionalidad y comunicación de resultados.

**Integrantes:** Ovejero Cesar, Ruiz Mariano, Isaías Cazazola
**Comisión:** Nueva Esperanza
**Fecha:** 04-07-26

## Objetivo del proyecto
Aplicar los contenidos de Minería de Datos 1 para construir un proyecto de análisis de datos reproducible, con decisiones justificadas y trazabilidad del proceso. El trabajo cubre la inspección inicial, la preparación de los datos, el análisis exploratorio univariado, bivariado y multivariado, y la reducción de dimensionalidad mediante PCA. No incluye modelado predictivo. Los resultados se comunican mediante una aplicación en Streamlit y un informe final breve en PDF.

## Dataset
El dataset (`data/raw/streaming_users_dirty.json`) contiene 8.160 registros de usuarios de una plataforma de streaming, con las siguientes columnas: `user_id`, `age`, `subscription_plan`, `monthly_watch_time_mins`, `country`, `favorite_genre`, `last_login_date` y `customer_support_tickets`.

Es un dataset con errores de carga intencionales (categorías inconsistentes, duplicados, valores fuera de rango, formatos de fecha mixtos y valores nulos), documentados en `notebooks/01_inspeccion_inicial.ipynb`.

## Estructura del repositorio
- `data/raw/`: dataset original sin modificar.
- `data/processed/`: dataset final utilizado en el análisis.
- `notebooks/`: desarrollo ordenado del proyecto (inspección, limpieza, EDA, PCA, conclusiones).
- `app/`: aplicación pública en Streamlit.
- `reports/`: informe final en PDF.
- `logs/`: registro de transformaciones del proceso ETL.

## Preparación y calidad de datos
A partir de la inspección inicial se aplicaron las siguientes decisiones, documentadas con evidencia en `notebooks/02_calidad_y_limpieza.ipynb`:
- Eliminación de 126 filas exactamente duplicadas y de 34 `user_id` repetidos con datos conflictivos (se conserva la primera aparición).
- Estandarización de categorías con variantes de escritura en `subscription_plan`, `country` y `favorite_genre`.
- Unificación de `last_login_date` a un único formato de fecha; 64 fechas inválidas o irrecuperables se dejaron como nulas.
- Valores imposibles en `age`, `monthly_watch_time_mins` y `customer_support_tickets` (negativos o fuera de todo rango plausible) marcados como nulos puntuales, preservando el resto del registro.
- No se imputaron valores numéricos automáticamente, para no fabricar información; se documentó como decisión pendiente para el Hito 4 si el PCA lo requiere.

El dataset final (`data/processed/streaming_users_clean.csv`) quedó con 8.000 filas (98.04% de retención). Detalle completo en `logs/pipeline_log.csv`.

## Resumen del análisis exploratorio
Análisis completo en `notebooks/03_eda.ipynb`, guiado por preguntas concretas:
- **Consumo mensual:** distribución con cola derecha; la mayoría consume 490–1.040 min/mes, con usuarios de alto consumo hasta ~4.200 min.
- **Planes:** 45% Básico, 35% Estándar, 20% Premium.
- **Consumo según plan:** relación clara y creciente (Básico ≈ 598 min, Estándar ≈ 872 min, Premium ≈ 1.140 min).
- **Tickets según plan:** sin relación; el promedio es prácticamente igual en los tres planes (~0.8).
- **Consumo por plan y país:** el patrón por plan se mantiene estable en los 7 países; el país aporta poca variación adicional.

El plan de suscripción resultó ser la variable más relevante para explicar diferencias de consumo.

## Reducción de dimensionalidad
Se aplicó PCA sobre las tres variables numéricas (`age`, `monthly_watch_time_mins`, `customer_support_tickets`), previamente escaladas con `StandardScaler` (detalle en `notebooks/04_pca.ipynb`). Las 3 componentes explican una varianza casi idéntica (~33% cada una), lo que confirma que las variables originales ya eran casi independientes entre sí: PCA no reduce la dimensionalidad de forma efectiva en este dataset. Aun así, PC2 resultó equivalente al consumo mensual y separa claramente a los usuarios por plan de suscripción.

## Visualización interactiva
La aplicación pública en Streamlit permite explorar el dataset, el análisis exploratorio y el PCA de forma interactiva.
Enlace: _(completar con el enlace de Streamlit Cloud)_

## Cómo ejecutar localmente
```bash
git clone <url-del-repositorio>
cd PI_Mineria_Datos_1
pip install -r requirements.txt
streamlit run app/Home.py
```

## Conclusiones
El consumo mensual de contenido es, con diferencia, la variable que mejor caracteriza a los usuarios según su plan de suscripción; la edad, el país y los tickets de soporte no mostraron relación clara con el plan. El PCA confirmó que las variables numéricas son casi independientes entre sí, por lo que no logra reducir la dimensionalidad de forma efectiva. Limitaciones y próximos pasos detallados en `notebooks/05_conclusiones.ipynb`.

---
**Enlaces:** [Repositorio GitHub](#) · [Aplicación Streamlit](#) · [Informe final](reports/informe_final.pdf) · [Log ETL](logs/pipeline_log.csv)
