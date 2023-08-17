import streamlit as st
import pickle
import numpy as np
from PIL import Image, ImageEnhance

image_path = "DTA Logo.png"
logo = Image.open(image_path)
new_size = (150, 100)
logo = logo.resize(new_size)

def load_model():
    with open('vineyard.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
melbourne_model = data['model']

def show_predicton():
    st.title("Vineyard Evaporation Prediction Model")
    max_temp = st.slider("Maximum temperature",5,35,15)
    rainfall = st.slider("Rainfall",0,16,5)
    windgust = st.slider("Windgust",15,60,35)
    humidity = st.slider("Relative humidity",40,100,70)
    ok = st.button("Calculate Evaporation")
    if ok:
        X = np.array([[max_temp, rainfall, windgust, humidity]])
        X = X.astype(float)
        
        evaporation = melbourne_model.predict(X)
        st.subheader(f"The estimated evaporation is {evaporation[0]:.2f}")
        
    # DTA logo
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        st.image(logo, use_column_width=False, width=new_size[0])
