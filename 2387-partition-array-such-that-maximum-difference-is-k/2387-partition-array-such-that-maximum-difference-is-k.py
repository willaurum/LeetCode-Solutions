class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        numSubs = 1
        first = nums[0]
        for i in nums:
            if i - first > k:
                numSubs += 1 
                first = i
        return numSubs
    