class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        scrap = []  
        carry = 0

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            total = bit_a + bit_b + carry
            scrap.append(total % 2)
            carry = total // 2

            i -= 1
            j -= 1

        scrap.reverse()
        lst = []
        for i in range(len(scrap)):
            lst.append(scrap[i])

        res = "".join(str(x) for x in lst)
        return res
