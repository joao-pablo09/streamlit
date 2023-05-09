import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt



# Lee el archivo CSV y crea un dataframe en Pandas
df = pd.read_csv('inventario.csv')
df['Precio x unidad'] = pd.to_numeric(df['Precio x unidad']) # convierte la columna a tipo numérico
st.title("Shine Details")

interfax = st.sidebar.radio("Por favor, seleccione la modalidad", ("Dulces", "Materiales", "Pedidos", "ganancias"))
if interfax == "Dulces":
    st.header("Dulces de Shine Details:")

    # mostrar la tabla de datos
    st.table(df)


    with st.form('Agregar productos'):
        productos = []
        for i, producto in df.iterrows():
            cantidad = st.number_input(f'Ingrese la cantidad de {producto["Nombre"]}', key=f'{i}_cantidad', min_value=0)
            if cantidad > 0:
                productos.append({'Nombre': producto['Nombre'], 'Precio x unidad': producto['Precio x unidad'],'Precio de venta': producto['Precio de venta'],'Cantidad': cantidad})
    
        # agregar un botón para enviar el formulario
        submit_button = st.form_submit_button('Comprar')

    # mostrar la lista de productos seleccionados y su cantidad
    if submit_button and len(productos) > 0:
        st.write('Productos seleccionados:')
        for producto in productos:
            st.write(f'{producto["Cantidad"]} x {producto["Nombre"]}')
        total = sum(producto['Precio x unidad'] * producto['Cantidad'] for producto in productos)
        total_venta = sum(producto['Precio de venta'] * producto['Cantidad'] for producto in productos)
        st.write(f'Se invirtió: {total:.2f}') # formatea el resultado para mostrar 2 decimales
        st.write(f'Precio total: {total_venta:.2f}') # formatea el resultado para mostrar 2 decimales
        ganancia=total_venta-total
        st.write(f'La ganancia en los dulce es : {ganancia:.2f}') # formatea el resultado para mostrar 2 decimales
if interfax=="Materiales":
    st.header("Materiales de Shine Details:")
    df = pd.read_excel('inventario_tota.xlsx', sheet_name='Materiales')
    st.table(df)




if interfax=="Pedidos":
    st.header("Pedidos de Shine Details:")
    st.header("Dia de la Madre")
    df_ped= pd.read_csv('pedidos.csv')
    image1 = Image.open('Corazon.jpeg')
    col1, col2 = st.columns(2)
    with col1:
        st.header("Caja Corazon")
        st.image(image1, caption="Figura 1: Pedido de corazon")
        suma_precios = df_ped['Precio'].sum()
        suma_compra = df_ped['Se compro'].sum()
        st.write(f'Se vendio en {suma_precios:.2f}')
        st.write(f'Se invirtio:{suma_compra:.2f}')
        ganancia=suma_precios-suma_compra
        st.write(f'La ganancia es de :{ganancia:.2f}')
    with col2:
        st.header("Lista de Dulces")
        st.table(df_ped)
    image2 = Image.open('Caja rosada.jpeg')
    image3 = Image.open('Arreglo Frutal.jpeg')
    col1, col2= st.columns(2)
    with col1:
        st.header("Caja Rosada")
        st.image(image2, caption="Figura 2: Pedido de caja rosada")
        st.write(f'Se vendio en 96.00')
        st.write(f'Se invirtio 70.25')
        st.write('Ganancia es 26.75')
    with col2:
        st.header("Arreglo Frutal")
        st.image(image3, caption="Figura 3: Pedido Arreglo Frutal")
        st.write('Se vendio en 110.00')
        st.write('Se invirtio 85.3')
        st.write('Ganancia es 24.7')
    
        





if interfax=="ganancias":
    st.header("Ganancias de Shine Details:")
    ganancias = pd.read_csv('ganancia.csv')
    # Gráfico de barras con las ganancias por pedido
    fig, ax = plt.subplots()
    ax.bar(ganancias['Nombre del pedido'], ganancias['Ganancia'])
    ax.set_xlabel('Pedidos')
    ax.set_ylabel('Ganancia')
    ax.set_title('Ganancia de cada pedido')
    st.pyplot(fig)
















