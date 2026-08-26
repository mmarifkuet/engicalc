def calculate_ideal_gas_pressure(n, R, T, V):
    """Calculates pressure using Ideal Gas Law: P = (n * R * T) / V"""
    if V == 0:
        return 0.0
    return (n * R * T) / V

def calculate_thermal_efficiency(work_output, heat_input):
    """Calculates thermal efficiency: eta = (W / Q_in) * 100"""
    if heat_input == 0:
        return 0.0
    return (work_output / heat_input) * 100.0