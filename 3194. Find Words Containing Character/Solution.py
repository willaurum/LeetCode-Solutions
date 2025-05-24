class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        out = []

        for i in range(len(words)):
            
            currentWord = words[i]
            digCount = len(currentWord)
            
            for char in range(digCount):
                if currentWord[char] == x:
                    out.append(i)
                    break
                else: 
                    continue

        return(out)
