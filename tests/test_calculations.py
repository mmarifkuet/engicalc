import pytest
from calculations.mechanics import calculate_force, calculate_torque, calculate_power
from calculations.fluid import calculate_flow_rate, calculate_reynolds_number
from calculations.heat_transfer import calculate_conduction_heat_transfer, calculate_convection_heat_transfer
from calculations.thermodynamics import calculate_ideal_gas_pressure, calculate_thermal_efficiency

def test_mechanics():
    assert calculate_force(10, 9.81) == pytest.approx(98.1)
    assert calculate_torque(100, 0.5) == pytest.approx(50.0)
    assert calculate_power(10, 10) == pytest.approx(100.0)

def test_fluid():
    assert calculate_flow_rate(2.0, 0.05) == pytest.approx(0.1)
    assert calculate_reynolds_number(1000, 1.5, 0.1, 0.001) == pytest.approx(150000.0)

def test_heat_transfer():
    assert calculate_conduction_heat_transfer(45.0, 2.0, 50.0, 0.05) == pytest.approx(90000.0)
    assert calculate_convection_heat_transfer(25.0, 1.5, 30.0) == pytest.approx(1125.0)

def test_thermodynamics():
    assert calculate_ideal_gas_pressure(1.0, 8.314, 300.0, 0.025) == pytest.approx(99768.0)
    assert calculate_thermal_efficiency(500.0, 1000.0) == pytest.approx(50.0)