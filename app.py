import streamlit as st
import pandas as pd
import joblib
from PIL import Image
from sklearn.metrics import mean_absolute_error

# Carregar o modelo treinado
model = joblib.load('melbourne_model.joblib')

# Configurar a página
st.set_page_config(
    page_title="Previsão de Preços de Imóveis em Melbourne",
    layout="centered"
)

# Adicionar um título e uma descrição
st.title("Previsão de Preços de Imóveis em Melbourne 🏠")
st.write("""
Insira os detalhes da casa para prever o preço estimado.
""")

# Carregar uma imagem (opcional)
# Adicionar uma imagem local ou da internet
from PIL import Image
import streamlit as st

# Tente carregar a imagem da pasta 'imagem'
try:
    image = Image.open('./imagem/house2.jpeg')  # Caminho relativo para a imagem
    st.image(image, use_column_width=True)  # Exibir a imagem no Streamlit
except FileNotFoundError:
    st.write("Imagem não encontrada, exibindo uma imagem da web.")
    st.image("https://vidrado.com/noticias/arquitetura-e-engenharia/casa-boutique-na-australia-por-cambuild/", use_column_width=True)  # URL alternativa

# Criar inputs para o usuário na barra lateral
st.sidebar.header("Insira os detalhes da casa:")

def user_input_features():
    rooms = st.sidebar.slider('Número de Quartos', 1, 10, 3)
    bathroom = st.sidebar.slider('Número de Banheiros', 1, 10, 2)
    landsize = st.sidebar.slider('Área do Terreno (m²)', 500.0, 10000.0, 1000.0)
    latitude = st.sidebar.slider('Latitude', -38.5, -37.5, -37.8)
    longitude = st.sidebar.slider('Longitude', 144.5, 145.5, 144.9)
    
    data = {
        'Rooms': rooms,
        'Bathroom': bathroom,
        'Landsize': landsize,
        'Lattitude': latitude,    
        'Longtitude': longitude   
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Exibir os inputs do usuário
st.subheader('Detalhes da Casa Inseridos')
st.write(input_df)

# Previsão do preço
if st.button('Prever Preço'):
    prediction = model.predict(input_df)
    
    # Calcular MAE com os dados inseridos
    actual_price = [500000]  # Exemplo de preço real; substitua conforme necessário
    mae_value = mean_absolute_error(actual_price, prediction)
    
    st.subheader('Preço Estimado da Casa')
    st.write(f"AUD {prediction[0]:,.2f}")
    
    st.subheader('Erro Médio Absoluto (MAE)')
    st.write(f"AUD {mae_value:,.2f}")
