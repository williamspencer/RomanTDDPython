from unittest import TestCase
import Roman

class KnownRoman(TestCase):

    def test_roman_forOne(self):
        result = Roman.romanToInt(1)
        expected = "I"
        self.assertEqual(expected, result)

    def test_roman_forTwo(self):
        result = Roman.romanToInt(2)
        expected = "II"
        self.assertEqual(expected, result)

    def test_roman_forThree(self):
        result = Roman.romanToInt(3)
        expected = "III"
        self.assertEqual(expected, result)

    def test_roman_forFour(self):
        result = Roman.romanToInt(4)
        expected = "IV"
        self.assertEqual(expected, result)

    def test_roman_forFive(self):
        result = Roman.romanToInt(5)
        expected = "V"
        self.assertEqual(expected, result)

    def test_roman_forSix(self):
        result = Roman.romanToInt(6)
        expected = "VI"
        self.assertEqual(expected, result)

    def test_roman_forSeven(self):
        result = Roman.romanToInt(7)
        expected = "VII"
        self.assertEqual(expected, result)

    def test_roman_forEight(self):
        result = Roman.romanToInt(8)
        expected = "VIII"
        self.assertEqual(expected, result)

    def test_roman_forNine(self):
        result = Roman.romanToInt(9)
        expected = "IX"
        self.assertEqual(expected, result)

    def test_roman_forTen(self):
        result = Roman.romanToInt(10)
        expected = "X"
        self.assertEqual(expected, result)

    def test_roman_forEleven(self):
        result = Roman.romanToInt(11)
        expected = "XI"
        self.assertEqual(expected, result)