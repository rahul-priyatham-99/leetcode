def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    str_num = str(x)
    reversed_num = str_num[::-1]
    if str_num == reversed_num:
        return True
    else:
        return False


output = isPalindrome(x=12100)
print(output)
