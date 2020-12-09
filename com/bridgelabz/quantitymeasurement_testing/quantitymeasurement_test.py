from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.Yard import Yard
from com.bridgelabz.quantitymeasurement.Inch import Inch
import pytest


# Test_case1 : For compare 3ft = 1yd
def test_givenTwoYardValue_WhenCompared_ShouldReturnTrue1():
    first_feet = Feet(3.0)
    second_yard = Yard(1.0)
    assert first_feet == second_yard
