def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j
    # new_list = []
    # count = 0
    # for i in nums:
    #     if i != val:
    #         new_list.append(i)
    # if len(new_list) != len(nums):
    #     new_list = new_list + [0] * (len(nums) - len(new_list))
    # for x in new_list:
    #     if x != 0:
    #         count += 1
    # return count


output = removeElement([3, 2, 2, 3, 3, 4], 4)
print(output)
