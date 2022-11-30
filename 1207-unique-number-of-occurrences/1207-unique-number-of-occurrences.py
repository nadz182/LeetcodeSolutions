class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashSet = Counter()
        for n in arr:
            hashSet[n] = 1 + hashSet.get(n,0)
        s = set()
        for n in hashSet.values():
            if n in s:
                return False
            s.add(n)
        return True