class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        vowels = ('a', 'e', 'i', 'o', 'u')
        s1 = s[:n//2]
        s2 = s[n//2:]
        count1, count2 = 0,0
        for i in range(n//2):
            if s1[i] in vowels:
                count1 += 1
            if s2[i] in vowels:
                count2 += 1
        
        return count1 == count2