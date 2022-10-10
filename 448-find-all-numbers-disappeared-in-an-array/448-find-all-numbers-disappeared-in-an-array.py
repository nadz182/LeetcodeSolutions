class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        missingNumbers = []
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+= 1
        
        for i in range(len(nums)):
            if i+1 != nums[i]:
                missingNumbers.append(i+1)
        return missingNumbers