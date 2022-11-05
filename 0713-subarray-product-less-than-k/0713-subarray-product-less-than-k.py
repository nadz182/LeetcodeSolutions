class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        sub_arrays = 0
        product = 1
        left = 0
        result = 0

        for right in range(len(nums)):
            product *= nums[right]
            sub_arrays += 1
            while (product >= k and left<= right):
                product /= nums[left]
                left += 1
                sub_arrays -= 1
            
            if product < k:
                result += sub_arrays

        return result