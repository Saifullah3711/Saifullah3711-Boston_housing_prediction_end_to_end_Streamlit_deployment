import streamlit as st
import numpy as np
from joblib import dump, load

model = load("HousingPrice.joblib") 


st.title("Housing Price Prediction - Boston Housing Project")

#============== Function to take input from user =========================
def User_input():

    CRIM = st.number_input(label="CRIM", step=1.0, format="%.2f")
    ZN = st.number_input(label="ZN", step=1.0, format="%.2f")
    INDUS = st.number_input(label="INDUS", step=1.0, format="%.2f")
    CHAS = st.number_input(label="CHAS", step=1.0, format="%.2f")
    NOX = st.number_input(label="NOX", step=1.0, format="%.2f")
    RM = st.number_input(label="RM", step=1.0, format="%.2f")
    AGE = st.number_input(label="AGE", step=1.0, format="%.2f")
    DIS = st.number_input(label="DIS", step=1.0, format="%.2f")
    RAD = st.number_input(label="RAD", step=1.0, format="%.2f")
    TAX = st.number_input(label="TAX", step=1.0, format="%.2f")
    PTRATIO = st.number_input(label="PTRATIO", step=1.0, format="%.2f")
    B = st.number_input(label=" B", step=1.0, format="%.2f")
    LSTAT = st.number_input(label="LSTAT", step=1.0, format="%.2f")
    
    resultant_np_array = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]])
   
    return resultant_np_array


values_for_model = User_input()
#----------------------------------------------------------------------------


#=========================== Prediction of Model ===============================
button_press = st.button("Predict")
if button_press:
   model_prediction = model.predict(values_for_model)
   st.title(f"Predicted Price is { model_prediction * 1000 }$")
#---------------------------------------------------------------------------------