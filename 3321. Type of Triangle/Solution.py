class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b > c and a + c > b and b + c > a:
            if a==b==c:
                return("equilateral")
            elif a != b and a != c and b != c:
                return("scalene")
            else:
                return("isosceles")
        else:
            return("none")