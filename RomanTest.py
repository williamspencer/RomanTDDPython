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

