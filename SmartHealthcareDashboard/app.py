import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load example healthcare data
data = {
    "Pregnancies": [6, 1, 8, 1, 0],
    "Glucose": [148, 85, 183, 89, 137],
    "BloodPressure": [72, 66, 64, 66, 40],
    "SkinThickness": [35, 29, 0, 23, 35],
    "Insulin": [0, 0, 0, 94, 168],
    "BMI": [33.6, 26.6, 23.3, 28.1, 43.1],
    "DiabetesPedigreeFunction": [0.627, 0.351, 0.672, 0.167, 2.288],
    "Age": [50, 31, 32, 21, 33],
    "Outcome": [1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = RandomForestClassifier()
model.fit(X_scaled, y)

# ---------------- UI ----------------
st.set_page_config(page_title="Smart Healthcare Dashboard", layout="centered")
st.title("🩺 Smart Healthcare Prediction & Analytics")

# Input form
st.header("👤 Patient Input")
with st.form("patient_form"):
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose", 0, 200, 120)
    blood_pressure = st.number_input("Blood Pressure", 0, 150, 70)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.number_input("Insulin", 0, 1000, 80)
    bmi = st.number_input("BMI", 0.0, 80.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.number_input("Age", 1, 120, 35)
    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame([{
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("⚠️ Likely to have diabetes")
    else:
        st.success("✅ Unlikely to have diabetes")

# ---------------- Charts ----------------
st.header("📊 Data Visualizations")

# 1. Outcome distribution
st.subheader("🧪 Outcome Distribution")
fig1 = px.histogram(df, x="Outcome", color="Outcome", nbins=2, title="Diabetes vs Non-Diabetes")
st.plotly_chart(fig1)

# 2. Age vs Outcome
st.subheader("👵 Age vs Outcome")
fig2 = px.bar(df, x="Age", y="Outcome", color="Outcome", title="Outcome by Age")
st.plotly_chart(fig2)

# 3. Glucose Level Histogram
st.subheader("🍬 Glucose Level Distribution")
fig3, ax3 = plt.subplots()
ax3.hist(df['Glucose'], bins=5, color='orange', edgecolor='black')
ax3.set_title("Glucose Distribution")
ax3.set_xlabel("Glucose Level")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# 4. Show raw data
with st.expander("📋 Show Raw Data"):
    st.dataframe(df)
