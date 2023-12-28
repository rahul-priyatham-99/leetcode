def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    words = s.split()
    reversed_words = ' '.join(reversed(words))
    print(type(reversed_words))
    return reversed_words


output = reverseWords(s="  hello world  ")
print(output)
