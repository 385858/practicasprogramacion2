import streamlit as st
st.title("Mi aplicacion para calcular el area figuras geométricas")
import math
# Widget para ingresar el radio
st.subtitle("Cálculo de área de un círculo")
radio= st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Calculo del area
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El area del circulo con radio {radio} es: {area: .2f}")

# Widget para ingresar base y altura
base= st.slider("Selecciona la base", 0.0, 10.0, 5.0)
altura= st.slider("Selecciona la altura", 0.0, 10.0, 5.0)
