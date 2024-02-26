import pandas as pd 
import plotly.express as px 
import streamlit as st 

car_data = pd.read_csv('vehicles.csv') #lendo os dados
hist_button = st.button('Criar histograma') #criar um botão
graf_button = st.button('Criar gráfico de dispersão') #criar um botão

st.header('Clique no botão acima para iniciar')

if hist_button: #se o botão for clicado
    #escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    #criar um histograma
    fig = px.histogram(car_data, x="odometer")

if graf_button: #se o botão for clicado
    #escrever uma mensagem
    st.write('Criando gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    #exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão

    #exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)