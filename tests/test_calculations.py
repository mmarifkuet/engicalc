import pytest
from calculations.mechanics import calculate_force, calculate_torque, calculate_power
from calculations.fluid import calculate_flow_rate, calculate_reynolds_number

def test_mechanics():
    assert calculate_force(10, 9.81) == pytest.approx(98.1)
    assert calculate_torque(100, 0.5) == pytest.approx(50.0)
    assert calculate_power(10, 10) == pytest.approx(100.0)

def test_fluid():
    assert calculate_flow_rate(2.0, 0.05) == pytest.approx(0.1)
    assert calculate_reynolds_number(1000, 1.5, 0.1, 0.001) == pytest.approx(150000.0)