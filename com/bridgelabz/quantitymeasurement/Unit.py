import enum


class Unit(enum.Enum):
    FEET = 12.0
    YARD = 36.0
    INCH = 1.0
    CM = 0.4
    GALLON = 3.78
    LITRE = 1
    ML = 0.001
    KG = 1.0
    GRAMS = 0.001
    TONNE = 1000
    FAHRENHEIT = 212
    CELSIUS = 100

    def __init__(self, unit):
        self.unit = unit

    def convert(self, length):
        """

        :param length: value of unit
        :return: convert the length
        """
        return self.unit * length

    def converttemp(self, temp):
        """

        :param temp: Fahrehein and Celsius
        :return: convert the temperature
        """
        if temp == Unit.CELSIUS:
            return (temp * 9 / 5) + 32
        elif temp == Unit.FAHRENHEIT:
            return temp * self.unit / 212
        return False
