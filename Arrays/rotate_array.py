def rotate1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    # reversing the given array
    l, r = 0, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    # reversing the elements in array from 0th index to k - 1
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    # reversing the elements in array from index k to last index position
    l, r = k, n - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
    print(nums)


def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    print(k)
    nums = nums[-k:] + nums[:-k]
    return nums


def rotate3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    i = 0
    while i < k:
        temp = nums.pop()
        nums.insert(0, temp)
        i += 1
    return nums


int_array = [1, 2, 3, 4, 5, 6, 7]
rotating_count = 3
output = rotate3(int_array, rotating_count)
print(output)
