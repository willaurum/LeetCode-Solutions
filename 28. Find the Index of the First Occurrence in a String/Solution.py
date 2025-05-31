class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        chk= False
        needlelength = len(needle)
        haylength = len(haystack)
        i = 0
        while i < haylength:
            if not chk and haystack[i:i+needlelength] == needle:
                chk = True
                return(i)
            i += 1

        if chk == False:
            return(-1)