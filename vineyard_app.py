import streamlit as st
from predict_page import show_predicton
from dashboard import show_dashboard

page = st.sidebar.selectbox("Explore or Predict",("Explore","Predict"))

if page == "Explore":
    show_dashboard()
else:
    show_predicton()
