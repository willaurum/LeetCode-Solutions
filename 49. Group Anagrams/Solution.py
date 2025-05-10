from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        answer = []

        for i in strs:
            sort = tuple(sorted(i))
            anagrams[sort].append(i)

        for v in anagrams.values():
            answer.append(v)

        return answer