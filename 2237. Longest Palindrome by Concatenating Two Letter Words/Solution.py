class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        length = 0
        used = set()
        has_center = False

        for word in list(word_count):
            rev_word = word[::-1]

            if word == rev_word:
            
                pairs = word_count[word] // 2
                length += pairs * 2 * len(word)

                if word_count[word] % 2 == 1:
                    has_center = True

            elif rev_word in word_count and word not in used and rev_word not in used:
                
                pairs = min(word_count[word], word_count[rev_word])
                length += pairs * 2 * len(word)
                used.add(word)
                used.add(rev_word)

        if has_center:
            length += len(word)  

        return(length)