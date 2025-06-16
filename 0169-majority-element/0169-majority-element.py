class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numcount = {}
        for num in nums:
            if num in numcount:
                numcount[num] += 1
            else:
                numcount[num] = 1

        return max(numcount, key=numcount.get)