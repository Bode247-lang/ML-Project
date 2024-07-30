# -*- coding: utf-8 -*-
"""
Created on Sunday July  28 4:00 AM 2024

@author: BODE
"""

import numpy as np
import pickle
import streamlit as st

# #loading the saved model
loaded_model = pickle.load(open("diabetes.pkl", "rb"))


def diabetes_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand I am making prediction for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"


def main():

    # giving the app a title
    st.title("Diabetes Web App")

    # getting the input data from user

   Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')


    # code for Prediction
    diagnosis = ''

    # creating a button for prediction

    if st.button("Diabetes Prediction Web App"):
        performance = performance_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
         st.success(diagnosis)


if __name__ == "__main__":
    main()
