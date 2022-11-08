class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack and ((c.isupper() and stack[-1] == c.lower()) or (c.islower() and stack[-1] == c.upper())):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)