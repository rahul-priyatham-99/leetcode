def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    roman_numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    result = ""
    for i in range(len(values)):
        while num >= values[i]:
            result = result + roman_numerals[i]
            num = num - values[i]
    return result


output = intToRoman(num=1994)
print(output)
