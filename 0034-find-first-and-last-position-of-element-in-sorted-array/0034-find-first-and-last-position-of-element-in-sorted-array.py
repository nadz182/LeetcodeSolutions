class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(findMaxInd):
            keyInd = -1
            start, end = 0, len(nums)-1
            
            while start <= end:
                mid = start + (end-start)//2
                if target < nums[mid]:
                    end = mid-1
                elif target > nums[mid]:
                    start = mid+1
                else:
                    keyInd = mid
                    if findMaxInd:
                        start = mid+1
                    else:
                        end = mid-1
            return keyInd
        
        
        result = [-1,-1]
        result[0] = binarySearch(False)
        if result[0] != -1:
            result[1] = binarySearch(True)
        return result