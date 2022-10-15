class Solution:
    def isHappy(self, n: int) -> bool:
        
        def findSquare(n):
            _sum = 0
            while n>0:
                digit = n%10
                _sum += digit*digit
                n //=10
            return _sum
        
        fast, slow = n,n
        while True:
            slow = findSquare(slow)
            fast = findSquare(findSquare(fast))
            if slow == fast:
                break
        return slow==1