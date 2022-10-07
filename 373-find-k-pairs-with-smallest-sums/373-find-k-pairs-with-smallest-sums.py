class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        maxHeap = []
        res = []
        
        for i in range(0, min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-(nums1[i]+nums2[j]), i, j))
                else:
                    if nums1[i]+nums2[j] > -maxHeap[0][0]:
                        break
                    else:
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, (-(nums1[i]+nums2[j]), i, j))
        for (num, i, j) in maxHeap:
            res.append([nums1[i], nums2[j]])
        return res