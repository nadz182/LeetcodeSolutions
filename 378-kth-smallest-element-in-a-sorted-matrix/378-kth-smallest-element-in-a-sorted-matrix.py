from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        
        for i in range(len(matrix)):
            heapq.heappush(minHeap, (matrix[i][0],0,matrix[i]))
        
        numCount, num = 0,0
        while minHeap:
            num, i , l = heapq.heappop(minHeap)

            numCount += 1
            if numCount == k:
                break
            if len(l) > i+1:
                heapq.heappush(minHeap, (l[i+1], i+1,l))
        return num