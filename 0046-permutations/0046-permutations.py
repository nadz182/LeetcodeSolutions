class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = deque()
        permutations.append([])
        
        for curNumber in nums:
            n = len(permutations)
            
            for _ in range(n):
                oldPerm = permutations.popleft()
                for j in range(len(oldPerm)+1):
                    newPerm = list(oldPerm)
                    newPerm.insert(j, curNumber)
                    if len(newPerm) == len(nums):
                        res.append(newPerm)
                    else:
                        permutations.append(newPerm)
        return res