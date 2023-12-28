def merge_sorted_arrays(nums1, m, nums2, n):
    """
    :param nums1:
    :param m:
    :param nums2:
    :param n:
    :return:
    """
    pointer = len(nums1) - 1
    m = m - 1
    n = n - 1

    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[pointer] = nums1[m]
            m -= 1
            pointer -= 1
        else:
            nums1[pointer] = nums2[n]
            n -= 1
            pointer -= 1
    if n >= 0:
        nums1[:n + 1] = nums2[:n + 1]
    print(nums1)


arr1 = [1, 2, 3, 0, 0, 0, 0]
arr2 = [2, 3, 4, 5]
len1 = 3
len2 = 4
merge_sorted_arrays(arr1, len1, arr2, len2)
