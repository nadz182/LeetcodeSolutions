class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start, end =0, len(arr)-1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if target == arr[mid]:
                return mid
            if arr[start] <= arr[mid]:
                if target>= arr[start] and target < arr[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target > arr[mid] and target <= arr[end]:
                    start = mid+1
                else:
                    end = mid-1
        return -1