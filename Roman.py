def romanToInt(value):
    result = ""
    while (value > 0):
        result += "I"
        value -= 1
    return result

    """if value == 3:
        return "III"
    elif value == 2:
        return "II"
    else:
        return "I" """