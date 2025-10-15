import streamlit as st
st.title("Mi aplicacion para calcular el area y perímetro de figuras geométricas")
import math
# Widget para ingresar el radio
st.title("Cálculo de área de un círculo")
radio= st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Calculo del area
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El area del circulo con radio {radio} es: {area: .2f}")

# 1. Selección de la figura
figura = st.selectbox("Selecciona una figura geométrica:", ("Círculo", "Triángulo", "Rectángulo", "Cuadrado"))
