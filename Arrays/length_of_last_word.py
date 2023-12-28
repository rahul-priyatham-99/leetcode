def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    if ' ' not in s:
        last_word = s
    else:
        last_word = s.split()[-1]
    print(last_word)
    count = len(last_word)
    return count


output = lengthOfLastWord("   fly me   to   the moon  ")
print(output)
