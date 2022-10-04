class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        charfreq = {}
        
        for n in nums:
            charfreq[n] = charfreq.get(n,0) + 1
            
        minHeap = []
        for char, freq in charfreq.items():
            heapq.heappush(minHeap, (freq, -char))
        
        res = []
        
        while minHeap:
            freq, char = heapq.heappop(minHeap)
            for _ in range(freq):
                
                res.append(-char)
        
        return res