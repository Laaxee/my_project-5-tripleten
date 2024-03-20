import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Exploración de datos de anuncios de venta de coches')

# Botón para construir un histograma
hist_button = st.button('Construir histograma')

if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear una columna 'color' basada en el tipo de combustible
    car_data['color'] = car_data['fuel'].apply(lambda x: 'Gasolina' if x == 'gas' else 'Diésel')
    
    # Crear un gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color='color',
                             labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)', 'color': 'Tipo de Combustible'},
                             title='Relación entre el Odómetro y el Precio de los Vehículos por Tipo de Combustible')
    
    # Personalizar el aspecto del gráfico de dispersión
    fig_scatter.update_traces(marker_size=8, opacity=0.7)
    fig_scatter.update_layout(xaxis_title='Odómetro (millas)', yaxis_title='Precio (USD)')
    
    # Mostrar un gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)





