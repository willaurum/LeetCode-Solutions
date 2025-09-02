import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        pairs = []
        for i in range(1, int(math.sqrt(area)) + 1):
            if area % i == 0:
                j = area // i
                pair = [max(i, j), min(i, j)]
                pairs.append(pair)
        #print(pairs)

        if len(pairs) == 1:
            return(pairs[0])
        else:
            differences = []
            for a, b in pairs:
                x = a-b
                differences.append(x)
            small = differences[0]
            #print(differences)
            min_index = 0
            for idx, r in enumerate(differences):
                if r < small:
                    small = r
                    min_index = idx
            return(pairs[min_index])


