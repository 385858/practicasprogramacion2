import streamlit as st
st.title("Mi aplicacion para calcular el area y perímetro de figuras geométricas")
import math
import matplotlib.pyplot as plt 
# Widget para ingresar el radio
st.title("Cálculo de área de un círculo")
radio= st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Calculo del area
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El area del circulo con radio {radio} es: {area: .2f}")

### Parte 1

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


elif figura == "Triángulo":
    base = st.number_input("Ingresa la base", min_value=0.1)
    altura = st.number_input("Ingresa la altura", min_value=0.1)
    lado_a = st.number_input("Ingresa el lado a", min_value=0.1)
    lado_b = st.number_input("Ingresa el lado b", min_value=0.1)
    lado_c = st.number_input("Ingresa el lado c", min_value=0.1)
    area = 0.5 * base * altura
    perimetro = lado_a + lado_b + lado_c

elif figura == "Rectángulo":
    base = st.number_input("Ingresa la base", min_value=0.1)
    altura = st.number_input("Ingresa la altura", min_value=0.1)
    area = base * altura
    perimetro = 2 * (base + altura)

elif figura == "Cuadrado":
    lado = st.number_input("Ingresa el lado", min_value=0.1)
    area = lado**2
    perimetro = 4 * lado

# 3. Mostrar los resultados
if area is not None and perimetro is not None:
    st.success(f"📐 Área: {area:.2f}")
    st.success(f"📏 Perímetro: {perimetro:.2f}")

    # También se pueden mostrar con st.metric
    st.metric(label="Área", value=f"{area:.2f}")
    st.metric(label="Perímetro", value=f"{perimetro:.2f}")

### Parte 2
