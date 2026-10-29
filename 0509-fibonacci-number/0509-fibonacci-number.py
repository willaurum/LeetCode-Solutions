class Solution:
    def fib(self, n: int) -> int:
        c=0
        a,b=0,1
        while c != n:
            d=a
            a=a+b
            b=d
            c+=1
        return a 