from com.bridgelabz.quantitymeasurement.QuantityMeasurement import *
import pytest


# UC-1
# Test_case for Feet
# Test_case1 : comparing two feet value
def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
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
    with pytest.raises(AssertionError):
        assert first_feet == second_feet


# Test_case5 : Comparing two different feet value
def test_givenZeroFeetAndOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Length.FEET, 0.0)
    second_feet = QuantityMeasurement(Length.FEET, 1.0)
    assert first_feet != second_feet


# Test_case for Yard
def test_givenZeroYardAndZeroYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard == second_yard


def test_givenZeroYardValueAndInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = first_yard
    assert first_yard == second_yard


def test_givenZeroYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    assert first_yard is not None


def test_givenZeroYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Length.YARD, 0.0)
    second_yard = float(0.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_yard


def test_givenZeroYardAndOneYard_WhenCompared_ShouldReturnFalse():
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
    with pytest.raises(AssertionError):
        assert first_inch == second_inch


def test_givenZeroInchAndOneInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Length.INCH, 0.0)
    second_inch = QuantityMeasurement(Length.INCH, 1.0)
    assert first_inch != second_inch


# UC-3
@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.FEET, 3.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 1.0), QuantityMeasurement(Length.YARD, 1.0), False),
                             (QuantityMeasurement(Length.INCH, 36.0), QuantityMeasurement(Length.YARD, 1.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.FEET, 3.0), True),
                             (QuantityMeasurement(Length.YARD, 1.0), QuantityMeasurement(Length.INCH, 36.0), True),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 5.0), True)

                         ])
def test_givenTwoLengthsUnitValue_WhenCompared_ShouldReturnExpected(first_length, second_length, expected):
    assert QuantityMeasurement.compareto(first_length, second_length) == expected


# UC-4
@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.INCH, 2.0), 4.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.INCH, 2.0), 14.0),
                             (QuantityMeasurement(Length.FEET, 1.0), QuantityMeasurement(Length.FEET, 1.0), 24.0),
                             (QuantityMeasurement(Length.INCH, 2.0), QuantityMeasurement(Length.CM, 2.5), 3.0),
                         ])
def test_givenTwoLengthsUnitValue_WhenAdd_ShouldReturnExpectedResult(first_length, second_length, expected):
    assert QuantityMeasurement.addition(first_length, second_length) == expected


# UC-5
@pytest.mark.parametrize("first_value, second_value, expected",
                         [
                             (QuantityMeasurement(Length.GALLON, 1.0), QuantityMeasurement(Length.LITRE, 3.78), True),
                         ])
def test_function(first_value, second_value, expected):
    assert QuantityMeasurement.compareto(first_value, second_value) == expected
