from unittest import TestCase
import Roman

class KnownRoman(TestCase):

    def test_roman_forOne(self):
        result = Roman.romanToInt(1)
        expected = "I"
