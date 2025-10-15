import streamlit as st
st.title("Mi aplicacion para calcular el area y perímetro de figuras geométricas🧮")
st.sidebar.write("Nombre: Octavio Hiram Juárez Lozoya") 
st.sidebar.write("Matrícula: 385858") 
import math
# Widget para ingresar el radio
st.title("Cálculo de área de un círculo")
radio= st.slider("Selecciona el radio", 0.0, 10.0, 5.0)

# Calculo del area
area = math.pi * radio**2

# Mostrar resultado
st.write(f"El area del circulo con radio {radio} es: {area: .2f}")

### Parte 1
st.title("Cálculo de area y perímetro de figuras geométricas")
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
import matplotlib.pyplot as plt
import streamlit as st
import math
import matplotlib.pyplot as plt

st.title("🧮 Calculadora de Área, Perímetro y Visualización")

figura = st.selectbox("Selecciona una figura:", ("Círculo", "Triángulo", "Rectángulo", "Cuadrado"))
color = st.color_picker("Elige un color para la figura", "#00f900")

area = perimetro = 0
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.axis("off")

if figura == "Círculo":
    r = st.slider("Radio", 0.1, 100.0, 10.0, key="radio")
    area = math.pi * r**2
    perimetro = 2 * math.pi * r
    ax.add_artist(plt.Circle((0, 0), r, color=color, fill=False, linewidth=2))
    ax.set_xlim(-r*1.2, r*1.2)
    ax.set_ylim(-r*1.2, r*1.2)

elif figura == "Triángulo":
    b = st.number_input("Base", min_value=0.1, key="base_tri")
    h = st.number_input("Altura", min_value=0.1, key="altura_tri")
    a = st.number_input("Lado a", min_value=0.1, key="a_tri")
    c = st.number_input("Lado c", min_value=0.1, key="c_tri")
    area = 0.5 * b * h
    perimetro = a + b + c
    ax.add_patch(plt.Polygon([[0, 0], [b, 0], [0, h]], color=color, fill=False, linewidth=2))
    ax.set_xlim(-1, b + 1)
    ax.set_ylim(-1, h + 1)

elif figura == "Rectángulo":
    b = st.number_input("Base", min_value=0.1, key="base_rect")
    h = st.number_input("Altura", min_value=0.1, key="altura_rect")
    area = b * h
    perimetro = 2 * (b + h)
    ax.add_patch(plt.Rectangle((0, 0), b, h, color=color, fill=False, linewidth=2))
    ax.set_xlim(-1, b + 1)
    ax.set_ylim(-1, h + 1)

elif figura == "Cuadrado":
    l = st.number_input("Lado", min_value=0.1, key="lado_cuad")
    area = l**2
    perimetro = 4 * l
    ax.add_patch(plt.Rectangle((0, 0), l, l, color=color, fill=False, linewidth=2))
    ax.set_xlim(-1, l + 1)
    ax.set_ylim(-1, l + 1)

# Mostrar resultados y figura
st.metric("Área", f"{area:.2f}")
st.metric("Perímetro", f"{perimetro:.2f}")
st.pyplot(fig)

### Parte 3
import numpy as np

st.set_page_config(page_title="Geometría y Trigonometría")

tab3 = st.tabs(["📈 Trigonometría"])

with tab3:
    st.title("Funciones Trigonométricas")
    rmax = st.slider("Rango (x)", math.pi, 10 * math.pi, 2 * math.pi)
    amp = st.slider("Amplitud", 0.1, 5.0, 1.0)
    x = np.linspace(0, rmax, 500)

    y_sin = amp * np.sin(x)
    y_cos = amp * np.cos(x)
    y_tan = amp * np.tan(x)
    y_tan[np.abs(y_tan) > 10] = np.nan  # Evitar saltos

    fig3, ax3 = plt.subplots()
    ax3.plot(x, y_sin, label="sin(x)")
    ax3.plot(x, y_cos, label="cos(x)")
    ax3.plot(x, y_tan, label="tan(x)")
    ax3.set_title("Trigonometría")
    ax3.grid(True)
    ax3.legend()

    st.pyplot(fig3)
