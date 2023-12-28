def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    previous_value = 0
    for i in reversed(s):
        current_value = romans[i]
        if current_value < previous_value:
            total = total - current_value
        else:
            total = total + current_value
        previous_value = current_value
    return total


output = romanToInt(s="MCMXCIV")
print(output)




