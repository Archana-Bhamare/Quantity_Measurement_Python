from com.bridgelabz.quantitymeasurement.Yard import Yard


class Inch:

    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Inch):
            if self.inch == other.inch:
                return True
        if isinstance(other, Yard):
            if self.inch == other.yard * 36:
                return True
        return False
