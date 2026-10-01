import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/bank_churn_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Bank Customer Churn Prediction")
st.write("Predict whether a bank customer is likely to churn.")

st.divider()

# Customer inputs
credit_score = st.number_input(
    "Credit Score",
    min_value=300,
    max_value=850,
    value=650
)

geography = st.selectbox(
    "Geography",
    ["France", "Germany", "Spain"]
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

tenure = st.number_input(
    "Tenure",
    min_value=0,
    max_value=10,
    value=5
)

balance = st.number_input(
    "Balance",
    min_value=0.0,
    value=50000.0
)

num_of_products = st.number_input(
    "Number of Products",
    min_value=1,
    max_value=4,
    value=1
)

has_cr_card = st.selectbox(
    "Has Credit Card?",
    ["Yes", "No"]
)

is_active_member = st.selectbox(
    "Is Active Member?",
    ["Yes", "No"]
)

estimated_salary = st.number_input(
    "Estimated Salary",
    min_value=0.0,
    value=50000.0
)

# Convert Yes/No to 1/0
has_cr_card_value = 1 if has_cr_card == "Yes" else 0
is_active_member_value = 1 if is_active_member == "Yes" else 0

# Create input dataframe
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Geography": [geography],
    "Gender": [gender],
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card_value],
    "IsActiveMember": [is_active_member_value],
    "EstimatedSalary": [estimated_salary]
})

# Prediction
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.divider()

    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is unlikely to churn")

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )