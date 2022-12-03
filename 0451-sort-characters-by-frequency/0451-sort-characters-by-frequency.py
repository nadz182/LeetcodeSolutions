class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(list(s))
        counter_sorted = sorted(counter, key=lambda x:counter[x], reverse=True)
        res = ""
        for c in counter_sorted:
            res += (counter[c] * c)
        return res