import streamlit as st
import numpy as np
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from PIL import Image, ImageEnhance

st.set_page_config(
    page_title="Vineyard Dashboard",
    page_icon="🍇",
    layout="wide"
)

# Custom CSS to enhance visual style
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f4f4f4;
        }
        .stButton {
            background-color: #009688;
            color: white;
        }
        .stTextInput {
            background-color: #ffffff;
            color: #333333;
        }
        .stMarkdown {
            color: #333333;
        }
        .stDataFrame {
            border-collapse: collapse;
            margin: 10px 0;
        }
        .stDataFrame th, .stDataFrame td {
            padding: 6px 12px;
            border: 1px solid #dddddd;
            text-align: left;
        }
        .stLineChart .highcharts-background {
            fill: transparent;
        }
        .custom-sidebar {
            position: relative;
        }
        .image-container {
            margin-left: auto;
            margin-right: 0;
            display: block;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
   
# Data fetching via API
api_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/birdwood  %2C%20south%20australia?unitGroup=metric&include=days&key=CBWQ6NTRW2GUF443E4WZ7XLGM&contentType=csv"
response = requests.get(api_url)
csv_data = response.content
df = pd.read_csv(io.BytesIO(csv_data))

# Correct date format
df['datetime'] = pd.to_datetime(df['datetime']).dt.strftime('%d-%m-%Y')
# Correct data type
df['datetime'] = pd.to_datetime(df['datetime'])
# Interpreted date format
df['interpreted_date'] = df['datetime'].dt.strftime('%d %B, %Y')
# Display today
first_datetime = df.loc[0, 'interpreted_date']


image_path = "DTA Logo.png"
logo = Image.open(image_path)
new_size = (150, 100)
logo = logo.resize(new_size)
    
def show_dashboard():
    # Create a Streamlit app
    st.title('🍇Vineyard Dashboard')
    
    st.write(f"Today: {first_datetime}")

    col1, col2 = st.columns(2)

    # Humidity Over Time chart
    with col1:
        st.subheader('Humidity Over Time')
        st.line_chart(df.set_index('datetime')['humidity'], use_container_width=True)

    # Temperature Over Time chart
    with col2:
        st.subheader('☀️Temperature Over Time')
        st.line_chart(df.set_index('datetime')['temp'], use_container_width=True)

    # DTA logo
    col1, col2, col3, col4, col5 = st.columns(5)
    with col5:
        st.image(logo, use_column_width=False, width=new_size[0])

    