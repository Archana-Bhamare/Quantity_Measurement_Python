from com.bridgelabz.quantitymeasurement.Unit import Unit


class QuantityMeasurement:
    def __init__(self, unit, value):
        self.unit = unit
        self.value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and other.value == self.value

    def compareto(self, other):
        """

        Compare Two unit
        :return: if units are equal then return true otherwise false
        """
        if isinstance(self.unit, Unit) and isinstance(other.unit, Unit):
            return Unit.convert(self.unit, self.value) == Unit.convert(other.unit, other.value)
        return False

    def compare(self, other):
        """

        Compare Fanhrehein and Celsius
        :return: when compare if equal then return true otherwise false
        """
        if isinstance(self.unit, Unit) and isinstance(other.unit, Unit):
            return Unit.converttemp(self.unit, self.value) == Unit.converttemp(other.unit, other.value)
        return False

    def __add__(self, other):
        return Unit.convert(self.unit, self.value) + Unit.convert(other.unit, other.value)
