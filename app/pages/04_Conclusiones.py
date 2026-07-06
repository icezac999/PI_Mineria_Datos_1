import streamlit as st

st.title("Conclusiones")

st.markdown("""
### Hallazgo principal
El **consumo mensual de contenido** es, con diferencia, la variable que mejor caracteriza a los
usuarios según su plan de suscripción (Básico ≈ 597 min, Estándar ≈ 872 min, Premium ≈ 1.140 min
en promedio). La edad, el país y los tickets de soporte no mostraron una relación clara con el
plan contratado.

El PCA confirmó esto desde otro ángulo: al no haber correlación entre las variables numéricas
originales, no existe una combinación de ellas que resuma mejor la información que el consumo por
sí solo.

### Limitaciones
- Los `user_id` duplicados con datos conflictivos se resolvieron conservando la primera
  aparición, sin poder verificar cuál registro era el correcto.
- Un pequeño grupo de edades muy bajas (0 y 4 años) no se trató como error por no contar con una
  regla clara para distinguirlo de un dato válido.
- Las variables disponibles son limitadas (no hay dispositivo, sesiones, motivo de baja, etc.).

### Próximos pasos
- Incorporar variables adicionales (dispositivo, sesiones, motivo de cancelación).
- Contar con una marca de tiempo de carga para resolver duplicados con un criterio más sólido.
- Explorar segmentación de usuarios (clustering) usando también `last_login_date`.

Detalle completo, con evidencia e interpretación de cada pregunta de análisis, en
`notebooks/05_conclusiones.ipynb`.
""")
