def romanToInt(value):
    result = ""
    if (value == 4):
        result = "IV"
        value -= 4
    while (value > 0):
        result += "I"
        value -= 1
    return result
