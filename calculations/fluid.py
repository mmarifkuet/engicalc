def calculate_flow_rate(velocity, area):
    """Calculates volumetric flow rate: Q = v * A"""
    return velocity * area

def calculate_reynolds_number(density, velocity, diameter, dynamic_viscosity):
    """Calculates Reynolds number: Re = (rho * v * D) / mu"""
    if dynamic_viscosity == 0:
        return 0.0
    return (density * velocity * diameter) / dynamic_viscosity