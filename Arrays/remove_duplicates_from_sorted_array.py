def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    print(nums)
    return j + 1


int_array = [1, 2, 3, 3, 3, 4, 4, 2, 1]
output = removeDuplicates(int_array)
print(output)
