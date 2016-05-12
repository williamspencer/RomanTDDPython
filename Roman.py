roman = {
    1 : "I",
    4 : "IV",
    5 : "V",
    9 : "IX",
    10 : "X"
    }

def romanToInt(value):
    result = ""

    for digit, numeral in sorted(roman.items(), reverse=True):
        while value >= digit:
            result += numeral
            value -= digit
    return result
