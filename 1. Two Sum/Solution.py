class Solution(object):
    def twoSum(self, nums, target):
        prevoiusMap = {} # value : index

        for i, n in enumerate(nums):
            difference = target - n

            if difference in prevoiusMap:
                return [prevoiusMap[difference], i]
            prevoiusMap[n] = i