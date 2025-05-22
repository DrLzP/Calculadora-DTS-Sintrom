
import streamlit as st
from datetime import datetime, timedelta

st.title("Calculadora de Dosis de Sintrom (DTS)")

# Entradas del usuario
inr_actual = st.number_input("INR actual", min_value=0.0, step=0.1)
inr_prev = st.number_input("INR previo", min_value=0.0, step=0.1)
dts_actual = st.number_input("DTS actual (mg/semana)", min_value=0.0, step=0.1)
fecha_actual = datetime.today()

ult_control_7_dias = st.checkbox("Último control hace ≤ 7 días")
cambios_clinicos = st.checkbox("Cambios clínicos o de medicación")

# Función de cálculo
def calcular_dts(inr_actual, inr_prev, dts_actual):
    if inr_actual <= 1.6:
        return dts_actual * 1.10
    elif inr_actual == 1.7:
        return dts_actual * 1.05
    elif inr_actual == 1.8:
        return dts_actual * 1.10
    elif inr_actual == 1.9:
        return dts_actual
    elif inr_actual == 2.3:
        return dts_actual
    elif 3.1 <= inr_actual <= 3.3:
        return dts_actual
    elif 3.4 <= inr_actual <= 3.6:
        return dts_actual * 1.05
    elif 3.7 <= inr_actual <= 3.9:
        return dts_actual * 1.10
    elif inr_actual >= 4:
        return dts_actual * 0.90
    else:
        return dts_actual

def calcular_pc(inr_actual, inr_prev, fecha_actual, ult_control_7_dias, cambios_clinicos):
    if cambios_clinicos:
        return fecha_actual + timedelta(days=7)
    elif ult_control_7_dias:
        return fecha_actual + timedelta(days=14)

    if inr_actual in [1.7, 1.8, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9]:
        if inr_prev < 2 or inr_prev > 3:
            return fecha_actual + timedelta(days=14)
        else:
            return fecha_actual + timedelta(days=21)
    elif inr_actual == 1.9:
        return fecha_actual + timedelta(days=28)
    elif inr_actual == 2.3:
        if inr_prev < 2 or inr_prev > 3:
            return fecha_actual + timedelta(days=28)
        else:
            return fecha_actual + timedelta(days=35)
    elif 3.1 <= inr_actual <= 3.3:
        return fecha_actual + timedelta(days=28)
    elif inr_actual <= 1.6 or inr_actual >= 4:
        return fecha_actual + timedelta(days=14)
    else:
        return fecha_actual + timedelta(days=28)

# Botón de cálculo
if st.button("Calcular"):
    if inr_actual and inr_prev and dts_actual:
        nueva_dts = round(calcular_dts(inr_actual, inr_prev, dts_actual), 1)
        fecha_pc = calcular_pc(inr_actual, inr_prev, fecha_actual, ult_control_7_dias, cambios_clinicos)

        st.success(f"Nueva DTS: {nueva_dts} mg/semana")
        st.info(f"Fecha del próximo control: {fecha_pc.strftime('%Y-%m-%d')}")
    else:
        st.warning("Por favor, rellena todos los campos numéricos.")
