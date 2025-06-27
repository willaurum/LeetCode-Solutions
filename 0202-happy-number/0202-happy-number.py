class Solution:
    def isHappy(self, n: int) -> bool:
        strN = str(n)
        temp = 0
        used = []
        for i in range(len(strN)):
            temp += int(strN[i]) ** 2

        while temp not in used:
            used.append(temp)
            n = temp
            temp = 0
            strN = str(n)
            
            for i in range(len(strN)):
                temp += int(strN[i]) ** 2
            if temp == 1:
                return(True)
                
            if temp in used:
                return(False)
                

