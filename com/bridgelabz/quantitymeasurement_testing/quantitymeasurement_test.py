from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.Yard import Yard
from com.bridgelabz.quantitymeasurement.Inch import Inch


# Test_case1 : For compare 3ft = 1yd
def test_givenOneFeetAndOneYardValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(3.0)
    second_yard = Yard(1.0)
    assert first_feet == second_yard


# Test_case2 : For compare 1ft != 1yd
def test_givenOneFeetAndOneYardValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(1.0)
    second_yard = Yard(1.0)
    assert first_feet != second_yard


# Test_case3 : For compare 1in != 1yd
def test_givenOneInchAndOneYardValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(1.0)
    second_yard = Yard(1.0)
    assert first_inch != second_yard


def test_givenOneInchAndOneYardValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(36.0)
    second_yard = Yard(1.0)
    assert first_inch == second_yard
