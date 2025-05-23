class Solution:
    def mySqrt(self, x: int) -> int:
        oddNumber = 1
        count = 0
        while True:
            if x == 0:
                break
            elif x < 0:
                count -= 1
                break
            else:
                count += 1
                x = x - oddNumber
                oddNumber = oddNumber + 2
            
        return(count)