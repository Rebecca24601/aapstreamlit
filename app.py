import streamlit as st
import requests
import json

# Define the form and input fields
st.title("Prediction")
st.write("Predict your risk of getting heart disease")

form_data = {
    "Age": st.number_input("Age", min_value=0, max_value=120, value=0, step=1),
    "Gender": st.selectbox("Gender", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male"),
    "HeartDiseaseorAttack": st.selectbox("Had Heart Disease or Attack", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "HighBP": st.selectbox("High Blood Pressure", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "HighChol": st.selectbox("High Cholesterol", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "CholCheck": st.selectbox("Cholesterol Check", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "BMI": st.number_input("BMI", min_value=0.0, max_value=50.0, value=0.0, step=0.1),
    "Smoker": st.selectbox("Smoker", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "Stroke": st.selectbox("Stroke", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "Diabetes": st.selectbox("Diabetes", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "PhysActivity": st.selectbox("Physical Activity", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "HvyAlcoholConsump": st.selectbox("Heavy Alcohol Consumption", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "GenHlth": st.slider("General Health", min_value=0, max_value=5, value=0, step=1),
    "MentHlth": st.slider("Mental Health", min_value=0, max_value=30, value=0, step=1),
    "PhysHlth": st.slider("Physical Health", min_value=0, max_value=30, value=0, step=1),
    "DiffWalk": st.selectbox("Difficulty Walking", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes"),
    "Symptoms": st.text_area("Describe your symptoms or health concerns")
}

# Define the predict button
if st.button("Predict"):
    # Send a POST request to the backend API
    try:
        response = requests.post('http://127.0.0.1:5000/predictheartrisk', json=form_data)
        response.raise_for_status()
        prediction_result = response.json()
        
        # Display the prediction results
        st.write("## Prediction Result:")
        st.write(f"Has Heart Disease: {prediction_result.get('has_heart_disease', 'N/A')}")
        st.write(f"Positive Percentage: {prediction_result.get('positive_percentage', 'N/A')}")
        st.write(f"Negative Percentage: {prediction_result.get('negative_percentage', 'N/A')}")
        st.write(f"Advice: {prediction_result.get('advice', 'N/A')}")
    except requests.RequestException as e:
        st.error(f"Error: {e}")
