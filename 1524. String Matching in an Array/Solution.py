class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wordbank = []

        for word in words:
            counter = 0
            for i in range(len(words)):
                
                if word in words[i]:
                    counter += 1
                    if counter == 2:
                        wordbank.append(word)
        return(wordbank)