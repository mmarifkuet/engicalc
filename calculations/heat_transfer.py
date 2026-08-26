def calculate_conduction_heat_transfer(k, area, temp_diff, thickness):
    """Calculates conduction heat transfer rate (Fourier's Law): Q = (k * A * dT) / L"""
    if thickness == 0:
        return 0.0
    return (k * area * temp_diff) / thickness

def calculate_convection_heat_transfer(h, area, temp_diff):
    """Calculates convection heat transfer rate (Newton's Law of Cooling): Q = h * A * dT"""
    return h * area * temp_diff