class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse() # [9, 9, 9]
        digits[0] = digits[0]+1                     # [10, 9, 9]
        x = 1
        tot = len(digits) - 1 
        #check to make sure it doesnt need to carry over
        if digits[0] != 10:
            digits.reverse() 
            return(digits)
        else:
            for i in range(0, len(digits)-1):
                if digits[i] == 10:                 # [10, 9, 9]    [0, 10, 9]
                    digits[i]= 0                   # [0, 9, 9]     [0, 0, 9]
                    digits[i+1] += 1                # [0, 10 ,9]    [0, 0, 10]

            if digits[tot] == 10:
                digits[tot] = 0                   #               [0, 0, 0]
                digits.append(x)                    #               [0, 0, 0, 1]
            digits.reverse()                        #               [1, 0, 0, 0]
            return(digits)