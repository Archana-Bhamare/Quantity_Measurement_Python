from com.bridgelabz.quantitymeasurement.Feet import Feet
import pytest


# Test_case for Feet
def test_givenTwoFeetValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet
