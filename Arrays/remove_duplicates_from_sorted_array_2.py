def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    j = 1
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[j] = nums[i]
            j += 1
    print(nums)
    return j


int_array = [0, 0, 1, 1, 1, 1, 2, 3, 3]
output = removeDuplicates(int_array)
print(output)
