class Solution:
    def bitwiseComplement(self, n: int) -> int:
        count, num = 0, n
        if n == 0:
            return 1
        while num > 0:
            count += 1
            num = num >> 1
        
        allBitSet = pow(2, count) - 1
        
        return n ^ allBitSet