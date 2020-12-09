from com.bridgelabz.quantitymeasurement.Yard import Yard
class Feet:

    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            if self.feet == other.feet:
                return True
        if isinstance(other, Yard):
            if self.feet == other.yard * 3.0:
                return True
        return False