class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #There are 3 children 
        answer = 0
        for i in range(min(limit, n)+ 1):
            if n - i <= 2 * limit:
                answer += min(n - i, limit) - max(0, n - i - limit) + 1
        return answer