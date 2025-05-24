class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        char_count = {}

        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for i in ransomNote:
            if i in char_count:
                char_count[i] -= 1
                if char_count[i] < 0:
                    return False
            else:
                return False
            
        return True