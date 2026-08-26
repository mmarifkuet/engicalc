import streamlit as st
from calculations.mechanics import calculate_force, calculate_torque, calculate_power
from calculations.fluid import calculate_flow_rate, calculate_reynolds_number
from calculations.heat_transfer import calculate_conduction_heat_transfer, calculate_convection_heat_transfer
from calculations.thermodynamics import calculate_ideal_gas_pressure, calculate_thermal_efficiency

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
        mass = st.number_input("Mass (kg)", min_value=0.0, value=10.0)
        acceleration = st.number_input("Acceleration (m/s²)", min_value=0.0, value=9.81)

        if st.button("Calculate Force"):
            force = calculate_force(mass, acceleration)
            st.success(f"Force = {force:.2f} N")

    elif calculation == "Torque":
        st.subheader("Torque Calculator")
        force = st.number_input("Force (N)", min_value=0.0, value=100.0)
        radius = st.number_input("Radius (m)", min_value=0.0, value=0.5)

        if st.button("Calculate Torque"):
            torque = calculate_torque(force, radius)
            st.success(f"Torque = {torque:.2f} N·m")

    elif calculation == "Power":
        st.subheader("Power Calculator")
        torque = st.number_input("Torque (N·m)", min_value=0.0, value=10.0)
        angular_velocity = st.number_input("Angular velocity (rad/s)", min_value=0.0, value=10.0)

        if st.button("Calculate Power"):
            power = calculate_power(torque, angular_velocity)
            st.success(f"Power = {power:.2f} W")

elif category == "Fluid Mechanics":

    st.header("Fluid Mechanics")

    calculation = st.selectbox(
        "Select calculation",
        [
            "Flow Rate",
            "Reynolds Number"
        ]
    )

    if calculation == "Flow Rate":
        st.subheader("Volumetric Flow Rate Calculator")
        velocity = st.number_input("Velocity (m/s)", min_value=0.0, value=2.0)
        area = st.number_input("Cross-sectional Area (m²)", min_value=0.0, value=0.05)

        if st.button("Calculate Flow Rate"):
            flow_rate = calculate_flow_rate(velocity, area)
            st.success(f"Flow Rate (Q) = {flow_rate:.4f} m³/s")

    elif calculation == "Reynolds Number":
        st.subheader("Reynolds Number Calculator")
        density = st.number_input("Fluid Density (kg/m³)", min_value=0.0, value=1000.0)
        velocity = st.number_input("Flow Velocity (m/s)", min_value=0.0, value=1.5)
        diameter = st.number_input("Pipe Diameter (m)", min_value=0.0, value=0.1)
        viscosity = st.number_input("Dynamic Viscosity (Pa·s)", min_value=0.00001, value=0.001, format="%.5f")

        if st.button("Calculate Reynolds Number"):
            reynolds = calculate_reynolds_number(density, velocity, diameter, viscosity)
            st.success(f"Reynolds Number (Re) = {reynolds:.2f}")

            if reynolds < 2300:
                st.info("Flow Regime: **Laminar**")
            elif reynolds <= 4000:
                st.warning("Flow Regime: **Transient**")
            else:
                st.info("Flow Regime: **Turbulent**")

elif category == "Heat Transfer":

    st.header("Heat Transfer")

    calculation = st.selectbox(
        "Select calculation",
        [
            "Conduction",
            "Convection"
        ]
    )

    if calculation == "Conduction":
        st.subheader("Conduction Heat Transfer Calculator (Fourier's Law)")
        k = st.number_input("Thermal Conductivity (W/m·K)", min_value=0.0, value=45.0)
        area = st.number_input("Surface Area (m²)", min_value=0.0, value=2.0)
        temp_diff = st.number_input("Temperature Difference ΔT (K or °C)", min_value=0.0, value=50.0)
        thickness = st.number_input("Wall Thickness (m)", min_value=0.001, value=0.05)

        if st.button("Calculate Conduction Rate"):
            q_cond = calculate_conduction_heat_transfer(k, area, temp_diff, thickness)
            st.success(f"Heat Transfer Rate (Q) = {q_cond:.2f} W")

    elif calculation == "Convection":
        st.subheader("Convection Heat Transfer Calculator (Newton's Law)")
        h = st.number_input("Heat Transfer Coefficient (W/m²·K)", min_value=0.0, value=25.0)
        area = st.number_input("Surface Area (m²)", min_value=0.0, value=1.5)
        temp_diff = st.number_input("Temperature Difference ΔT (K or °C)", min_value=0.0, value=30.0)

        if st.button("Calculate Convection Rate"):
            q_conv = calculate_convection_heat_transfer(h, area, temp_diff)
            st.success(f"Heat Transfer Rate (Q) = {q_conv:.2f} W")

elif category == "Thermodynamics":

    st.header("Thermodynamics")

    calculation = st.selectbox(
        "Select calculation",
        [
            "Ideal Gas Law (Pressure)",
            "Thermal Efficiency"
        ]
    )

    if calculation == "Ideal Gas Law (Pressure)":
        st.subheader("Ideal Gas Law (P = nRT / V)")
        n = st.number_input("Amount of Substance n (moles)", min_value=0.0, value=1.0)
        R = st.number_input("Gas Constant R (J/mol·K)", min_value=0.0, value=8.314)
        T = st.number_input("Absolute Temperature T (K)", min_value=0.0, value=298.15)
        V = st.number_input("Volume V (m³)", min_value=0.001, value=0.024)

        if st.button("Calculate Pressure"):
            p = calculate_ideal_gas_pressure(n, R, T, V)
            st.success(f"Pressure (P) = {p:.2f} Pa ({p/1000:.2f} kPa)")

    elif calculation == "Thermal Efficiency":
        st.subheader("Thermal Efficiency Calculator (η = W / Q_in)")
        work = st.number_input("Work Output W (J or kJ)", min_value=0.0, value=500.0)
        q_in = st.number_input("Heat Input Q_in (J or kJ)", min_value=0.0, value=1200.0)

        if st.button("Calculate Efficiency"):
            eta = calculate_thermal_efficiency(work, q_in)
            st.success(f"Thermal Efficiency (η) = {eta:.2f}%")