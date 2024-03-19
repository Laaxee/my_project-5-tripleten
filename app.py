import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

# columna 'color' basada en el tipo de combustible
car_data['color'] = car_data['fuel'].apply(lambda x: 'Gasolina' if x == 'gas' else 'Diésel')

# gráfico de dispersión con Plotly Express
fig = px.scatter(car_data, x="odometer", y="price", color='color',
                 labels={'odometer': 'Odómetro (millas)', 'price': 'Precio (USD)', 'color': 'Tipo de Combustible'},
                 title='Relación entre el Odómetro y el Precio de los Vehículos por Tipo de Combustible')

# Personalizar el aspecto del gráfico
fig.update_traces(marker_size=8, opacity=0.7)

# Añadir título a los ejes x e y
fig.update_layout(xaxis_title='Odómetro (millas)', yaxis_title='Precio (USD)')

# Mostrar el gráfico de dispersión en Streamlit
st.plotly_chart(fig)
