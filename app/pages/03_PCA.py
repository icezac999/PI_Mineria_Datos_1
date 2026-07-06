import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

sns.set_style("whitegrid")
ORDEN_PLANES = ["Básico", "Estándar", "Premium"]

st.title("PCA")

df = pd.read_csv("data/processed/streaming_users_clean.csv")
vars_num = ["age", "monthly_watch_time_mins", "customer_support_tickets"]

st.markdown("""
**Variables utilizadas:** `age`, `monthly_watch_time_mins`, `customer_support_tickets`
(las únicas variables numéricas del dataset).

**Escalamiento aplicado:** `StandardScaler` (media 0, desvío 1), necesario porque las variables
tienen escalas muy distintas (años, minutos, cantidad de tickets). Para poder calcular el PCA,
los nulos de estas columnas se imputaron con la mediana solo para este análisis.
""")

imputer = SimpleImputer(strategy="median")
X = imputer.fit_transform(df[vars_num])
X_scaled = StandardScaler().fit_transform(X)

pca = PCA()
componentes = pca.fit_transform(X_scaled)
varianza = pca.explained_variance_ratio_

st.subheader("Varianza explicada")
tabla = pd.DataFrame({
    "Componente": [f"PC{i+1}" for i in range(3)],
    "Varianza explicada": varianza.round(3),
})
st.dataframe(tabla, hide_index=True)

st.caption(
    "Las 3 componentes explican una proporción casi idéntica de la varianza (~33% cada una). "
    "Esto confirma que las variables originales ya eran casi independientes entre sí: PCA no "
    "logra reducir la dimensionalidad de forma efectiva en este dataset."
)

st.subheader("Usuarios proyectados en PC1 y PC2")
df_pca = df.copy()
df_pca["PC1"] = componentes[:, 0]
df_pca["PC2"] = componentes[:, 1]

fig, ax = plt.subplots()
sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="subscription_plan", hue_order=ORDEN_PLANES,
                 palette="viridis", alpha=0.4, s=20, ax=ax)
ax.axhline(0, color="gray", linewidth=0.5)
ax.axvline(0, color="gray", linewidth=0.5)
st.pyplot(fig)

st.caption(
    "PC2 está dominada por el consumo mensual y separa claramente a los usuarios por plan "
    "(Básico < Estándar < Premium). PC1 combina edad y tickets, y no separa a los planes: "
    "ninguna de las dos variables se relaciona con el plan contratado."
)
