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
# Variables para área y perímetro
area = None
perimetro = None

# 2. Mostrar solo los parámetros relevantes
if figura == "Círculo":
    radio = st.slider("Selecciona el radio", 0.1, 100.0, 10.0)
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    st.write(f"El area del circulo con radio {radio} es: {area: 2.f}")
    st.write(f"El perimetro de un circulo con radio {radio} es:")

