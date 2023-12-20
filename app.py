import streamlit as st
import pandas as pd
import requests
import json


# call the predictions through endpoint
def get_prediction(data):
    url = 'https://askai.aiclub.world/493ab8b4-f15e-46da-9c60-2aff0bf205e8'
    r = requests.post(url, data=json.dumps(data))
    response = getattr(r, '_content').decode("utf-8")
    print(response)
    return response


# web app
# title
st.title("Heart Disease Predictor")

# setting the image
st.image("doctor-drawing-heart2.jpg", caption="Heart Disease")

# expander to say about the project
with st.expander("About the Project 📑"):
    st.subheader("The Project")
    st.markdown(
        "- This project is mainly focused on predicting the possibility of having a Heart Disease")

# tabs to navigate
tab1, tab2 = st.tabs(["Introduction 📊", "Predictions 💻"])

with tab1:
    st.subheader("Dataset")
    # reading the dataset
    data1 = pd.read_csv("Heart_Disease_Prediction.csv")
    st.dataframe(data1)

    # feature impotance
    st.subheader("Main Variables which impact the heart diseases")
    st.image("featureimportance.png", caption="Feature Importance")

with tab2:
    st.header("Prediction Dashboard")
    st.markdown("- User can fill the form.")
    st.markdown("- The predictions can be seen after completing the form")

    # prediction dashboard
    # get the link
    st.subheader("Predict the Possibility of having a Heart Disease")
    st.subheader("Please fill the form below")

    # Get inputs from the user
    sex = st.selectbox("Sex:", ["Male", "Female"])
    if sex == 'Male':
        sex = 1
    elif sex == 'Female':
        sex = 0
    chest_pain_type = st.selectbox("Chest Pain Type:", ["1", "2", "3", "4"])
    age = st.slider("Age:", min_value=1, max_value=120, value=25)
    cholesterol = st.slider("Cholesterol:", min_value=100, max_value=500, value=200)
    fbs_over_120 = st.selectbox("FBS Over 120:", ["Yes", "No"])
    if fbs_over_120 == 'Yes':
        fbs_over_120 = 1
    elif fbs_over_120 == 'No':
        fbs_over_120 = 0
    bp = st.slider("BP:", min_value=80, max_value=200, value=120)
    max_hr = st.slider("Max HR:", min_value=50, max_value=250, value=150)
    exercise_angina = st.selectbox("Exercise Angina:", ["Yes", "No"])
    if exercise_angina == 'Yes':
        exercise_angina = 1
    elif exercise_angina == 'No':
        exercise_angina = 0
    ekg_results = st.selectbox("EKG Results::", ["0", "1", "2"])
    slope_of_st = st.selectbox("Thallium:", ["Upsloping", "Flat", "Downsloping"])
    if slope_of_st == 'Upsloping':
        slope_of_st = 1
    elif slope_of_st == 'Flat':
        slope_of_st = 2
    elif slope_of_st == 'Downsloping':
        slope_of_st = 3
    num_vessels_fluro = st.slider("Number Of Vessels Fluro:", min_value=0, max_value=3, value=0)
    st_depression = st.text_input("ST Depression:", "Enter a value")
    thallium = st.selectbox("Thallium:", ["Normal", "Fixed Defect", "Reversible Defect"])
    if thallium == 'Normal':
        thallium = 3
    elif thallium == 'Fixed Defect':
        thallium = 6
    elif thallium == 'Reversible Defect':
        thallium = 7

    # Button to start predictions
    if st.button("Predict"):
        # Store user inputs in a dictionary
        input_data = {
            'Sex': int(sex),
            'Chest pain type': int(chest_pain_type),
            'Age': int(age),
            'Cholesterol': int(cholesterol),
            'FBS over 120': int(fbs_over_120),
            'BP': int(bp),
            'Max HR': int(max_hr),
            'Exercise angina': int(exercise_angina),
            'EKG results': int(ekg_results),
            'Slope of ST': int(slope_of_st),
            'Number of vessels fluro': int(num_vessels_fluro),
            'ST depression': float(st_depression),
            'Thallium': int(thallium),
        }
        print(input_data)

        # Getting the predictions
        response = get_prediction(input_data)
        response = json.loads(response)
        print(response)
        response = json.loads(response['body'])
        prediction = response['predicted_label']
        if prediction == 'Absence':
            st.subheader('No trace of having Heart Disease.')
        elif prediction == 'Presence':
            st.subheader('Have traces of Heart Disease.')
