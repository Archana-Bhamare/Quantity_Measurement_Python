from com.bridgelabz.quantitymeasurement.QuantityMeasurement import *
import pytest


# UC-1
# Test_case for Feet
# Test_case1 : comparing two feet value
def test_givenZeroFtAndZeroFt_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Unit.FEET, 0.0)
    second_feet = QuantityMeasurement(Unit.FEET, 0.0)
    assert first_feet == second_feet


# Test_case2 : Comparing Two instance feet variable
def test_givenZeroFtInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Unit.FEET, 0.0)
    second_feet = first_feet
    assert first_feet == second_feet


# Test_Case3 : Comparing one feet value should return false when None
def test_givenZeroFtValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Unit.FEET, 0.0)
    assert first_feet is not None


# Test_case4 : Compared one feet value with float value
def test_givenZeroFeetAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_feet = QuantityMeasurement(Unit.FEET, 0.0)
    second_feet = float(0.0)
    with pytest.raises(AssertionError):
        assert first_feet == second_feet


# Test_case5 : Comparing two different feet value
def test_givenZeroFeetAndOneFeet_WhenCompared_ShouldReturnFalse():
    first_feet = QuantityMeasurement(Unit.FEET, 0.0)
    second_feet = QuantityMeasurement(Unit.FEET, 1.0)
    assert first_feet != second_feet


# Test_case for Yard
def test_givenZeroYardAndZeroYard_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Unit.YARD, 0.0)
    second_yard = QuantityMeasurement(Unit.YARD, 0.0)
    assert first_yard == second_yard


def test_givenZeroYardValueAndInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Unit.YARD, 0.0)
    second_yard = first_yard
    assert first_yard == second_yard


def test_givenZeroYardValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Unit.YARD, 0.0)
    assert first_yard is not None


def test_givenZeroYardAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_yard = QuantityMeasurement(Unit.YARD, 0.0)
    second_yard = float(0.0)
    with pytest.raises(AssertionError):
        assert first_yard == second_yard


def test_givenZeroYardAndOneYard_WhenCompared_ShouldReturnFalse():
    first_yard = QuantityMeasurement(Unit.YARD, 0.0)
    second_yard = QuantityMeasurement(Unit.YARD, 1.0)
    assert first_yard != second_yard


# Test_case for Inch
def test_givenZeroInchandZeroInchValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Unit.INCH, 0.0)
    second_inch = QuantityMeasurement(Unit.INCH, 0.0)
    assert first_inch == second_inch


def test_givenZeroInchValueInstanceVariable_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Unit.INCH, 0.0)
    second_inch = first_inch
    assert first_inch == second_inch


def test_givenZeroInchValue_WhenComparedIfNotNone_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Unit.INCH, 0.0)
    assert first_inch is not None


def test_givenZeroInchAndFloatValue_WhenCompared_ShouldReturnTrue():
    first_inch = QuantityMeasurement(Unit.INCH, 0.0)
    second_inch = float(0.0)
    with pytest.raises(AssertionError):
        assert first_inch == second_inch


def test_givenZeroInchAndOneInch_WhenCompared_ShouldReturnFalse():
    first_inch = QuantityMeasurement(Unit.INCH, 0.0)
    second_inch = QuantityMeasurement(Unit.INCH, 1.0)
    assert first_inch != second_inch


# UC2-3 : Compare Lengths
@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Unit.FEET, 3.0), QuantityMeasurement(Unit.YARD, 1.0), True),
                             (QuantityMeasurement(Unit.FEET, 1.0), QuantityMeasurement(Unit.YARD, 1.0), False),
                             (QuantityMeasurement(Unit.INCH, 1.0), QuantityMeasurement(Unit.YARD, 1.0), False),
                             (QuantityMeasurement(Unit.INCH, 36.0), QuantityMeasurement(Unit.YARD, 1.0), True),
                             (QuantityMeasurement(Unit.YARD, 1.0), QuantityMeasurement(Unit.FEET, 3.0), True),
                             (QuantityMeasurement(Unit.YARD, 1.0), QuantityMeasurement(Unit.INCH, 36.0), True),
                             (QuantityMeasurement(Unit.INCH, 2.0), QuantityMeasurement(Unit.CM, 5.0), True)

                         ])
def test_givenTwoLengthsUnitValue_WhenCompared_ShouldReturnExpected(first_length, second_length, expected):
    assert QuantityMeasurement.compareto(first_length, second_length) == expected


# UC-4- Add Two lengths in inches
@pytest.mark.parametrize("first_length, second_length,expected",
                         [
                             (QuantityMeasurement(Unit.INCH, 2.0), QuantityMeasurement(Unit.INCH, 2.0), 4.0),
                             (QuantityMeasurement(Unit.FEET, 1.0), QuantityMeasurement(Unit.INCH, 2.0), 14.0),
                             (QuantityMeasurement(Unit.FEET, 1.0), QuantityMeasurement(Unit.FEET, 1.0), 24.0),
                             (QuantityMeasurement(Unit.INCH, 2.0), QuantityMeasurement(Unit.CM, 2.5), 3.0),
                         ])
def test_givenTwoLengthsUnitValue_WhenAdd_ShouldReturnExpectedResult(first_length, second_length, expected):
    assert first_length + second_length == expected


# UC-5-Compare Volumes in Litre and Gallon
@pytest.mark.parametrize("first_volume, second_volume, expected",
                         [
                             (QuantityMeasurement(Unit.GALLON, 1.0), QuantityMeasurement(Unit.LITRE, 3.78), True),
                             (QuantityMeasurement(Unit.LITRE, 1.0), QuantityMeasurement(Unit.ML, 1000.0), True),
                             (QuantityMeasurement(Unit.LITRE, 1.0), QuantityMeasurement(Unit.ML, 500.0), False),
                             (QuantityMeasurement(Unit.GALLON, 1.0), QuantityMeasurement(Unit.ML, 1000.0), False),
                         ])
def test_givenTwoVolumeUnitValue_WhenCompared_ShouldReturnExpected(first_volume, second_volume, expected):
    assert QuantityMeasurement.compareto(first_volume, second_volume) == expected


# UC6-Add Volumes in Litres
@pytest.mark.parametrize("first_volume, second_volume,expected",
                         [
                             (QuantityMeasurement(Unit.GALLON, 1.0), QuantityMeasurement(Unit.LITRE, 3.78), 7.56),
                             (QuantityMeasurement(Unit.LITRE, 1.0), QuantityMeasurement(Unit.ML, 1000), 2.0),
                         ])
def test_givenTwoVolumeUnitValue_WhenAdd_ShouldReturnExpectedResult1(first_volume, second_volume, expected):
    assert first_volume + second_volume == expected


# UC7-Compare and Add Weights in Gram
@pytest.mark.parametrize("first_weight, second_weight, expected",
                         [
                             (QuantityMeasurement(Unit.KG, 1.0), QuantityMeasurement(Unit.GRAMS, 1000), True),
                             (QuantityMeasurement(Unit.TONNE, 1.0), QuantityMeasurement(Unit.KG, 1000.0), True)
                         ])
def test_givenTwoWeightValue_WhenCompared_ShouldReturnExpected(first_weight, second_weight, expected):
    assert QuantityMeasurement.compareto(first_weight, second_weight) == expected


# Addition of Weight in Grams
@pytest.mark.parametrize("first_weight, second_weight,expected",
                         [
                             (QuantityMeasurement(Unit.TONNE, 1.0), QuantityMeasurement(Unit.GRAMS, 1000), 1001)
                         ])
def test_givenTwoWeightValue_WhenAdd_ShouldReturnExpectedResult1(first_weight, second_weight, expected):
    assert first_weight + second_weight == expected


# UC8-Equate Fahrenheit and Celsius
@pytest.mark.parametrize("first_temp, second_temp, expected",
                         [
                             (QuantityMeasurement(Unit.FAHRENHEIT, 212), QuantityMeasurement(Unit.CELSIUS, 100), True),
                             (QuantityMeasurement(Unit.CELSIUS, 100), QuantityMeasurement(Unit.FAHRENHEIT, 212), True)
                         ])
def test_GivenOneFahAndOneCelsius_WhenCompare_ShouldReturnTrue(first_temp, second_temp, expected):
    assert QuantityMeasurement.compare(first_temp, second_temp) == expected
