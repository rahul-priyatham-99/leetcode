# Moore's voting algorithm
# Time and Space efficient solution
import math


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    majority = nums[0]
    votes = 1
    for x in range(1, len(nums)):
        if votes == 0:
            votes += 1
            majority = nums[x]
        elif nums[x] == majority:
            votes += 1
        else:
            votes -= 1
    return majority


# using sorting method
def majorityElement2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    max_count = math.ceil(len(nums)/2)
    return nums[max_count]


# using hash_table method:
def majorityElement3(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    new_dict = {}
    for x in range(len(nums)):
        if nums[x] in new_dict:
            new_dict[nums[x]] += 1
        else:
            new_dict[nums[x]] = 1
    high_freq = max(new_dict.values())
    for key in new_dict:
        if high_freq == 1:
            return None
        else:
            if new_dict[key] == high_freq:
                return key
    return new_dict


int_array = [3, 3, 4, 5, 2]
output = majorityElement3(int_array)
print(output)
