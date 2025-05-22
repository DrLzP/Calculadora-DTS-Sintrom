# Calculadora Dosis Sintrom

Esta aplicación médica permite calcular la nueva **Dosis Total Semanal (DTS)** de Sintrom (acenocumarol) y la **fecha del próximo control (PC)**, en función del valor de INR actual, el valor previo y posibles excepciones clínicas.

### 🩺 Funcionalidad

- Ajuste automático de la DTS según el valor del INR actual.
- Cálculo de la fecha del próximo control:
  - Considera si el último control fue hace ≤ 7 días.
  - Considera si ha habido cambios clínicos o de medicación.
- Compatible con PC, tablet o móvil (vía Streamlit Cloud).

### 🧠 Lógica clínica aplicada

- Basada en algoritmo de ajuste por rangos de INR según protocolo PDF adjunto.
- Las **excepciones solo modifican la fecha de control**, pero **no alteran la dosis recomendada**.

### 📦 Requisitos

- Python 3.8+
- streamlit

### ▶️ Cómo ejecutar en local

```bash
pip install streamlit
streamlit run calculadora_sintrom_streamlit_v2.py
```

---

Creada por [@DrLzP](https://github.com/DrLzP) para uso médico-clínico.
