class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        closeToOpen = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }
        
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
                continue
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        return not stack