import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'model.pkl'  # Replace with your actual file name
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the app
st.title("Diabetes Prediction App")
st.write("Enter the required values to predict diabetes")

# Input fields for the required features
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0, max_value=120, step=1)
hypertension = st.selectbox("Hypertension (0 for No, 1 for Yes)", [0, 1])
heart_disease = st.selectbox("Heart Disease (0 for No, 1 for Yes)", [0, 1])
smoking_history = st.selectbox("Smoking History", ["never", "former", "current", "ever", "not current"])
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1)
hba1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, step=0.1)
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=500, step=1)

# Convert categorical variables to numeric values
gender = 1 if gender == "Male" else 0
smoking_history_dict = {"never": 0, "former": 1, "current": 2, "ever": 3, "not current": 4}
smoking_history = smoking_history_dict[smoking_history]

# Button to make prediction
if st.button("Predict"):
    # Prepare input data in the required shape
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 1:
        st.write("The model predicts that the patient has diabetes.")
    else:
        st.write("The model predicts that the patient does not have diabetes.")
