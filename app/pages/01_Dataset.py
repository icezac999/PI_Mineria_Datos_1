import streamlit as st
import pandas as pd

st.title("Dataset")

st.markdown("""
El dataset original contiene 8.160 registros de usuarios de una plataforma de streaming.
Presentaba filas duplicadas, categorías escritas de forma inconsistente, valores imposibles
(edades negativas, minutos de consumo fuera de todo rango plausible) y fechas en formatos
mixtos.

Tras el proceso de limpieza (ver `notebooks/02_calidad_y_limpieza.ipynb`), el dataset final
quedó con 8.000 filas. El detalle completo de cada transformación está en `logs/pipeline_log.csv`.
""")

df = pd.read_csv("data/processed/streaming_users_clean.csv")
st.dataframe(df.head(20))

