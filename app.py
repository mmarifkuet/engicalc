import streamlit as st

st.set_page_config(
    page_title="EngiCalc",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ EngiCalc")
st.write("Engineering Calculation Toolkit")

st.sidebar.header("Calculation")

category = st.sidebar.selectbox(
    "Select category",
    [
        "Mechanics",
        "Fluid Mechanics",
        "Heat Transfer",
        "Thermodynamics"
    ]
)

if category == "Mechanics":

    st.header("Mechanics")

    calculation = st.selectbox(
        "Select calculation",
        [
            "Force",
            "Torque",
            "Power"
        ]
    )

    if calculation == "Force":

        st.subheader("Force Calculator")

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

            st.success(
                f"Force = {force:.2f} N"
            )

    elif calculation == "Torque":

        st.subheader("Torque Calculator")

        force = st.number_input(
            "Force (N)",
            min_value=0.0,
            value=100.0
        )

        radius = st.number_input(
            "Radius (m)",
            min_value=0.0,
            value=0.5
        )

        if st.button("Calculate Torque"):

            torque = force * radius

            st.success(
                f"Torque = {torque:.2f} N·m"
            )

    elif calculation == "Power":

        st.subheader("Power Calculator")

        torque = st.number_input(
            "Torque (N·m)",
            min_value=0.0,
            value=10.0
        )

        angular_velocity = st.number_input(
            "Angular velocity (rad/s)",
            min_value=0.0,
            value=10.0
        )

        if st.button("Calculate Power"):

            power = torque * angular_velocity

            st.success(
                f"Power = {power:.2f} W"
            )

else:

    st.info(
        f"{category} calculations will be added soon."
    )