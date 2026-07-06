import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
ORDEN_PLANES = ["Básico", "Estándar", "Premium"]

st.title("Análisis Exploratorio (EDA)")

df = pd.read_csv("data/processed/streaming_users_clean.csv")

st.header("Univariado")

st.subheader("1. Distribución del consumo mensual")
fig, ax = plt.subplots()
sns.histplot(df["monthly_watch_time_mins"].dropna(), bins=40, color="#4C72B0", ax=ax)
ax.set_xlabel("Minutos de consumo mensual")
ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.caption(
    "La mayoría de los usuarios consume entre 490 y 1.040 minutos por mes, con un grupo "
    "minoritario de alto consumo que llega hasta ~4.200 minutos."
)

st.subheader("2. Distribución de planes de suscripción")
fig, ax = plt.subplots()
sns.countplot(data=df, x="subscription_plan", order=ORDEN_PLANES, hue="subscription_plan",
              palette="Blues_d", legend=False, ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("Cantidad de usuarios")
st.pyplot(fig)
st.caption("El plan Básico concentra el 45% de los usuarios, el Estándar el 35% y el Premium el 20%.")

st.header("Bivariado")

st.subheader("3. Consumo mensual según plan de suscripción")
fig, ax = plt.subplots()
sns.boxplot(data=df, x="subscription_plan", y="monthly_watch_time_mins", order=ORDEN_PLANES,
            hue="subscription_plan", palette="Blues_d", legend=False, ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("Minutos de consumo mensual")
st.pyplot(fig)
st.caption(
    "El consumo promedio sube de forma escalonada según el plan (Básico ≈ 598, Estándar ≈ 872, "
    "Premium ≈ 1.140 min), casi el doble entre los extremos."
)

st.subheader("4. Tickets de soporte según plan de suscripción")
fig, ax = plt.subplots()
sns.barplot(data=df, x="subscription_plan", y="customer_support_tickets", order=ORDEN_PLANES,
            hue="subscription_plan", palette="Blues_d", errorbar=None, legend=False, ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("Tickets de soporte (promedio)")
st.pyplot(fig)
st.caption(
    "A diferencia del consumo, acá no hay relación: el promedio de tickets es prácticamente "
    "igual en los tres planes (entre 0.79 y 0.81)."
)

st.header("Multivariado")

st.subheader("5. Consumo mensual según plan y país")
pivot = df.pivot_table(values="monthly_watch_time_mins", index="country",
                        columns="subscription_plan", aggfunc="mean")[ORDEN_PLANES].round(1)
fig, ax = plt.subplots()
sns.heatmap(pivot, annot=True, fmt=".0f", cmap="Blues", ax=ax)
ax.set_xlabel("Plan"); ax.set_ylabel("País")
st.pyplot(fig)
st.caption(
    "El patrón Básico < Estándar < Premium se repite en los 7 países sin excepciones: el plan "
    "explica más las diferencias de consumo que el país."
)

