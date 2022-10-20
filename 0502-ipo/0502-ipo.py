from heapq import *

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        minCapitalHeap = []
        maxProfitHeap = []
        
        for i in range(0, len(profits)):
            heapq.heappush(minCapitalHeap, (capital[i], i))
        
        availableCapital = w
        
        for _ in range(k):
            
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, (-profits[i], i))
            
            if not maxProfitHeap:
                break
            
            availableCapital += -heapq.heappop(maxProfitHeap)[0]
        return availableCapital