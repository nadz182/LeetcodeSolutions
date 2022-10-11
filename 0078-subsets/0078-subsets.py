class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        
        for curNumber in nums:
            n = len(subsets)
            for i in range(n):
                set1 = list(subsets[i])
                set1.append(curNumber)
                subsets.append(set1)
        return subsets
#time complexity: O(N * 2^N)
#space complexity: O(N * 2^N)