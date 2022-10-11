class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        permutations = []
        permutations.append(s)
        
        for i in range(len(s)):
            if s[i].isalpha():
                n = len(permutations)
                for j in range(n):
                    ch = list(permutations[j])
                    ch[i] = ch[i].swapcase()
                    permutations.append(''.join(ch))
        return permutations