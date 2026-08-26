import streamlit as st

st.set_page_config(
    page_title="EngiCalc",
    page_icon="⚙️"
)

st.title("⚙️ EngiCalc")
st.write("Engineering Calculation Toolkit")

st.header("Force Calculator")

mass = st.number_input(
    "Mass (kg)",
    min_value=0.0,
    value=10.0
)

acceleration = st.number_input(
    "Acceleration (m/s²)",
    min_value=0.0,
    value=9.81
)

if st.button("Calculate Force"):
    force = mass * acceleration
    st.success(f"Force = {force:.2f} N")
