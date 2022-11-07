class Solution:
    def maximum69Number (self, num: int) -> int:
        numList = []
        while num:
            digit = num%10
            numList.append(digit)
            num = num//10
        numList = numList[::-1]
        for i in range(len(numList)):
            if numList[i] == 6:
                numList[i] = 9
                return int(''.join(str(n) for n in numList))
        return int(''.join(str(n) for n in numList))