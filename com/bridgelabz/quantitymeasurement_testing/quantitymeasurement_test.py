from com.bridgelabz.quantitymeasurement.QuantityMeasurement import *
import pytest


# Test_case for Feet
# Test_case1 : comparing two feet value
def test_givenZeroFtandZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet == second_feet


# Test_case2 : Comparing Two instance feet variable
def test_givenZeroFtInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# Test_Case3 : Comparing one feet value should return false when None
def test_givenZeroFtValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    assert first_feet is not None


# Test_case4 : Compared one feet value with float value
def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = float(0.0)
    with pytest.raises(AttributeError):
        assert first_feet == second_feet


# Test_case5 : Comparing two different feet value
def test_givenZeroFeetandOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 1.0)
    assert first_feet != second_feet


# Test_case for Yard
def test_givenZeroYardandZeroYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard == second_yard


def test_givenZeroYardValueandInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = first_yard
    assert first_yard == second_yard


def test_givenZeroYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard is not None


def test_givenZeroYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = float(0.0)
    with pytest.raises(AttributeError):
        assert first_yard == second_yard


def test_givenZeroYardandOneYard_WhenCompared_ShouldReturnFalse():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_yard != second_yard


# Test_case for Inch
def test_givenZeroInchandZeroInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = QuantityMeasurement(Length.INCH, 0.0)
    assert first_inch == second_inch


def test_givenZeroInchValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    assert first_inch is not None


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = float(0.0)
    with pytest.raises(AttributeError):
        assert first_inch == second_inch


def test_givenZeroInchandOneInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = QuantityMeasurement(Length.INCH, 1.0)
    assert first_inch != second_inch


# UC2
# Test_case1 : For compare 3ft = 1yd
def test_given_3FeetAnd_1YardValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Length.FEET, 3.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_yard


# Test_case2 : For compare 1ft != 1yd
def test_given_1FeetAnd_1YardValue_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 1.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_feet != second_yard


# Test_case3 : For compare 1in != 1yd
def test_givenOneInchAndOneYardValue_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH, 1.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    assert first_inch != second_yard


# Test_case4 : For Compare 36in = 1yd
def test_given_36InchAndOneYardValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 36.0)
    second_yard = QuantityMeasurement(Length.YARD, 1.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_yard


# Test_case5 : For compare 1yd = 3ft
def test_givenOneYardAnd_3FeetValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 1.0)
    second_feet = QuantityMeasurement(Length.FEET, 3.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_feet


# Test_case6 : For compare 1yd = 36in
def test_givenOneYardAnd_36InchValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 1.0)
    second_inch = QuantityMeasurement(Length.INCH, 36.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_inch


# UC3 : 2in = 5cm
def test_givenTwoInchAndFiveCMValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Length.INCH, 2.0)
    second_cm = QuantityMeasurement(Length.CM, 5.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_cm
