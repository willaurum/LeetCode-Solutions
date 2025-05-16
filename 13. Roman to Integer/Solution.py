class Solution:
    def romanToInt(self, s: str) -> int:

        numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }


        total = 0
        prev = 0

        for i in reversed(s):
            current = numerals[i]
            if prev > current:
                total -= current
            else:
                total += current
            prev = current
        return(total)