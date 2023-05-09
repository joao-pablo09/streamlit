import streamlit as st
import pandas as pd

# Cargar datos de la tabla de dulces
df_dulces = pd.read_csv("dulces.csv")

# Título de la aplicación
st.title("Precios de dulces en Shine Details")

# Crear una tabla que muestre los precios de los dulces
st.write("Tabla de precios de los dulces:")
st.table(df_dulces[["Nombre", "Precio"]])
