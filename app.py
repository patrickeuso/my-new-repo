import streamlit as st
import pandas as pd
import plotly.express as px

# Defina o caminho do arquivo
file_path = r"C:\Users\HP\OneDrive\Desktop\Pessoal\Tripleten - Bootcamp\Modulo 5\Projeto 5\vehicles.csv"

# Leia os dados
car_data = pd.read_csv(file_path)

# Adicione um cabeçalho ao aplicativo Streamlit
st.header('Análise dos Dados de Veículos')

# Crie um botão para o histograma
hist_button = st.button('Criar histograma')

if hist_button: # se o botão for clicado
    # Escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Crie um botão para o gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button: # se o botão for clicado
    # Escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    
    # Criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Desafio extra: substituir botões por caixas de seleção
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: # se a caixa de seleção for selecionada
    st.write('Criando um gráfico de dispersão para as colunas odometer e price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
