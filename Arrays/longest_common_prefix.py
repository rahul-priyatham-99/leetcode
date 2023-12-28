def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    strs = sorted(strs)
    first_string = strs[0]
    last_string = strs[-1]

    prefix = ''
    for i in range(len(first_string)):
        if i < len(last_string) and first_string[i] == last_string[i]:
            prefix = prefix + first_string[i]
        else:
            break
    return prefix


output = longestCommonPrefix(strs=["flower", "flow", "flight"])
print(output)

