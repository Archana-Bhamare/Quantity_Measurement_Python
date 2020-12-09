from com.bridgelabz.quantitymeasurement.Feet import Feet
from com.bridgelabz.quantitymeasurement.Yard import Yard
from com.bridgelabz.quantitymeasurement.Inch import Inch
import pytest


# Test_case for Feet
# Test_case1 : comparing two feet value
def test_givenTwoFeetValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = Feet(0.0)
    assert first_feet == second_feet


# Test_case2 : Comparing Two instance feet variable
def test_givenTwoFeetValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# Test_Case3 : Comparing one feet value should return false when None
def test_givenOneFeetValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = Feet(0.0)
    assert first_feet is not None


# Test_case4 : Compared one feet value with float value
def test_givenOneFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = Feet(0.0)
    second_feet = float(0.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_feet


# Test_case5 : Comparing two different feet value
def test_givenTwoDifferentFeetValue_WhenCompared_ShouldReturnFalse():
    first_feet = Feet(0.0)
    second_feet = Feet(1.0)
    assert first_feet != second_feet


# Test_case for Yard
def test_givenTwoYardValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = Yard(0.0)
    assert first_yard == second_yard


def test_givenTwoYardValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = first_yard
    assert first_yard == second_yard


def test_givenOneYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = Yard(0.0)
    assert first_yard is not None


def test_givenOneYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(0.0)
    second_yard = float(0.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_yard


def test_givenTwoDifferentYardValue_WhenCompared_ShouldReturnFalse():
    first_yard = Yard(0.0)
    second_yard = Yard(1.0)
    assert first_yard != second_yard


# Test_case for Inch
def test_givenTwoInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = Inch(0.0)
    assert first_inch == second_inch


def test_givenTwoInchValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenOneInchValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_inch = Inch(0.0)
    assert first_inch is not None


def test_givenOneInchAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(0.0)
    second_inch = float(0.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_inch


def test_givenTwoDifferentInchValue_WhenCompared_ShouldReturnFalse():
    first_inch = Inch(0.0)
    second_inch = Inch(1.0)
    assert first_inch != second_inch


# UC2
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


# Test_case4 : For Compare 36in = 1yd
def test_givenOneInchAndOneYardValue_WhenCompared_ShouldReturnTrue():
    first_inch = Inch(36.0)
    second_yard = Yard(1.0)
    assert first_inch == second_yard


# Test_case5 : For compare 1yd = 3ft
def test_givenOneYardAndOneFeetValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(1.0)
    second_feet = Feet(3.0)
    assert first_yard == second_feet


# Test_case6 : For compare 1yd = 36in
def test_givenOneYardAndOneInchValue_WhenCompared_ShouldReturnTrue():
    first_yard = Yard(1.0)
    second_inch = Inch(36.0)
    assert first_yard == second_inch
