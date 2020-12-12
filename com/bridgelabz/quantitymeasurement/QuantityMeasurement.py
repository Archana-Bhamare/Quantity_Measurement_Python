from com.bridgelabz.quantitymeasurement.Unit import Unit


class QuantityMeasurement:
    def __init__(self, unit, length):
        self.unit = unit
        self.length = length

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurement):
            return self.unit == other.unit and other.length == self.length

    def compareto(self, other):
        if isinstance(self.unit, Unit) and isinstance(other.unit, Unit):
            return Unit.convert(self.unit, self.length) == Unit.convert(other.unit, other.length)
        return False

    def addition(self, other):
        return Unit.convert(self.unit, self.length) + Unit.convert(other.unit, other.length)