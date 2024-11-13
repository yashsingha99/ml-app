import streamlit as st
import pickle
import numpy as np

# Load the model
model_path = 'model.pkl'  # Replace with your actual file name
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define the app title and introduction
st.title("Diabetes Prediction App")
st.write(
    "This application predicts the likelihood of diabetes based on several health indicators. "
    "Please provide the following details:"
)

# Input fields for the required features with helpful tooltips
gender = st.selectbox("Gender", ["Male", "Female"], help="Select the gender of the patient.")
age = st.number_input("Age", min_value=0, max_value=120, step=1, help="Enter the age in years.")
hypertension = st.selectbox("Hypertension", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", 
                            help="Select 'Yes' if the patient has hypertension, otherwise 'No'.")
heart_disease = st.selectbox("Heart Disease", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No", 
                             help="Select 'Yes' if the patient has heart disease, otherwise 'No'.")
smoking_history = st.selectbox(
    "Smoking History", ["never", "former", "current", "ever", "not current"],
    help="Specify the patient's smoking history."
)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, step=0.1, help="Enter the BMI value.")
hba1c_level = st.number_input("HbA1c Level", min_value=0.0, max_value=20.0, step=0.1, 
                              help="Enter the HbA1c level as a percentage.")
blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, max_value=500, step=1, 
                                      help="Enter the blood glucose level in mg/dL.")

# Convert categorical variables to numeric values
gender = 1 if gender == "Male" else 0
smoking_history_dict = {"never": 0, "former": 1, "current": 2, "ever": 3, "not current": 4}
smoking_history = smoking_history_dict[smoking_history]

# Button to make prediction
if st.button("Predict Diabetes Risk"):
    # Prepare input data in the required shape
    input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
    prediction = model.predict(input_data)

    # Display the prediction result with a clearer message
    if prediction[0] == 1:
        st.error("The model predicts that the patient is at risk of diabetes.")
    else:
        st.success("The model predicts that the patient is not at risk of diabetes.")
