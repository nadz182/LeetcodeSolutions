class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = 0
        for n in nums:
            n1xn2 ^= n
        
        rightmostbit = 1
        
        while (rightmostbit & n1xn2) == 0:
            rightmostbit = rightmostbit << 1
        
        num1, num2 = 0, 0
        
        for n in nums:
            if (rightmostbit & n) != 0:
                num1 ^= n
            else:
                num2 ^= n
        return [num1, num2]