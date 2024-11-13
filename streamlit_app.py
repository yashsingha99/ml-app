import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# App title and description
st.title("Diabetes Prediction App")
st.markdown("### Predict the likelihood of diabetes based on health indicators.")
st.write("Please provide the following details to get a prediction.")

# Function to map categorical inputs
def map_inputs(gender, smoking_history):
    gender_val = 1 if gender == "Male" else 0
    smoking_history_dict = {"never": 0, "former": 1, "current": 2, "ever": 3, "not current": 4}
    smoking_history_val = smoking_history_dict[smoking_history]
    return gender_val, smoking_history_val

# Sidebar for user inputs
st.sidebar.header("Patient Details")
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.number_input("Age", min_value=0, max_value=120, step=1)
hypertension = st.sidebar.selectbox("Hypertension", ["No", "Yes"])
heart_disease = st.sidebar.selectbox("Heart Disease", ["No", "Yes"])
smoking_history = st.sidebar.selectbox("Smoking History", ["never", "former", "current", "ever", "not current"])
bmi = st.sidebar.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)
hba1c_level = st.sidebar.number_input("HbA1c Level", min_value=0.0, max_value=20.0, step=0.1)
blood_glucose_level = st.sidebar.number_input("Blood Glucose Level", min_value=0, max_value=500, step=1)

# Map inputs to required numeric values
gender, smoking_history = map_inputs(gender, smoking_history)
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

# Predict button
if st.sidebar.button("Predict Diabetes Risk"):
    # Prepare input data for prediction
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
    prediction = model.predict(input_data)

    # Display the prediction result
    st.write("### Prediction Result:")
    if prediction[0] == 1:
        st.error("The model predicts that the patient **has diabetes**.")
    else:
        st.success("The model predicts that the patient **does not have diabetes**.")
