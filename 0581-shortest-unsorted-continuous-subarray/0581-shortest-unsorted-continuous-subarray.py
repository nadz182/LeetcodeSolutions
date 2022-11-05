import math
class Solution:
    def findUnsortedSubarray(self, arr: List[int]) -> int:
        low, high = 0, len(arr)-1
        
        while (low < len(arr)-1 and arr[low] <= arr[low+1]):
            low += 1
        if low == len(arr)-1:
            return 0
        
        while (high > 0 and arr[high-1] <= arr[high]):
            high -=1 
        
        subarray_max = -math.inf
        subarray_min = math.inf
        
        for k in range(low, high+1):
            subarray_max = max(arr[k],subarray_max)
            subarray_min = min(arr[k],subarray_min)
        
        while (low > 0 and arr[low-1] > subarray_min):
            low -= 1
        while (high < len(arr)-1 and arr[high+1] < subarray_max):
            high += 1
        
        return high - low + 1