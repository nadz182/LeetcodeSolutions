class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numhash = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numhash:
                return [i, numhash[diff]]
            numhash[n] = i
        return []