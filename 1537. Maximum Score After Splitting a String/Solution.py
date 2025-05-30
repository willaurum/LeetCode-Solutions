class Solution:
    def maxScore(self, s: str) -> int:
        digs = len(s)
        ans = 0
        for i in range(1, digs):
            stringL = s[:i]
            stringR = s[i:]
            temp = 0
            for l in range(len(stringL)):
                if stringL[l] == "0":
                    temp += 1
            for r in range(len(stringR)):
                if stringR[r] == "1":
                    temp += 1

            if temp > ans:
                ans = temp

        return(ans)