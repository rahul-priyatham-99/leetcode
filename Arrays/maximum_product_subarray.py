class Solution:
    @staticmethod
    def maxProduct1(nums):  # This solution will exceed the time limit
        """
        :type nums: List[int]
        :return: int
        """
        sub_arrays = []
        products = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub_array = nums[i:j]
                sub_arrays.append(sub_array)
        for array in sub_arrays:
            product = 1
            for i in array:
                product = product * i
            products.append(product)
        return max(products)

    def maxProduct2(self, nums):  # This solution will not exceed the time limit
        """
        :param nums: List[int]
        :return: int
        """
        max_product = nums[0]
        min_product = nums[0]
        result = max_product
        if len(nums) <= 0:
            return 0
        for i in nums[1:]:
            if i < 0:
                max_product = min_product
                min_product = max_product
            max_product = max(i, max_product * i)
            min_product = min(i, min_product * i)
            result = max(result, max_product)
        return result


instance_of_class = Solution()
nums = [1, 2, 3, 4]  # other sample test cases are [2,3,-2,4], [-2,0,-1]
result1 = instance_of_class.maxProduct1(nums)
result2 = instance_of_class.maxProduct2(nums)
print(result1, result2)


