import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="House Price Predictor", layout="centered")

try:
    with open("house_model.pkl", "rb") as f:
        model = pickle.load(f)
except:
    st.error("Please upload house_model.pkl")

st.markdown("""
    <style>
    div[data-testid="stForm"] {
        border: 1px solid #e6e9ef !important;
        border-radius: 10px !important;
        padding: 30px !important;
        background-color: white !important;
    }
    .stNumberInput label {
        color: #31333F !important;
        font-weight: bold !important;
    }
    div.stButton > button {
        width: 100% !important;
        background-color: #1b6cfc !important;
        color: white !important;
        border: none !important;
        padding: 10px !important;
        font-weight: bold !important;
        border-radius: 4px !important;
    }
    div.stAlert {
        background-color: #e8f5e9 !important;
        color: #2e7d32 !important;
        border: 1px solid #c8e6c9 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🏠 House Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #70757a;'>Enter the details of the house below to predict its price:</p>", unsafe_allow_html=True)

with st.form("my_form"):
    area = st.number_input("Area (in sq ft)", value=500)
    st.caption("Enter the total area of the house in square feet")
    
    bedrooms = st.number_input("Number of Bedrooms", value=2)
    st.caption("Enter the number of bedrooms")
    
    bathrooms = st.number_input("Number of Bathrooms", value=1)
    st.caption("Enter the number of bathrooms")
    
    submit = st.form_submit_button("Predict Price")

if submit:
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ₹{prediction[0]:,.2f}")

