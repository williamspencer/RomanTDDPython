def romanToInt(value):
    result = ""
    roman = {
        "X": 10,
    }

    for i in roman:
        while value >= roman[i]:
            result += i
            value -= roman[i]

    if (value >= 10):
        result = "X"
        value -= 10
    if (value == 9):
        result = "IX"
        value -= 9
    if (value >= 5):
        result = "V"
        value -= 5
    if (value == 4):
        result = "IV"
        value -= 4
    while (value > 0):
        result += "I"
        value -= 1
    return result
