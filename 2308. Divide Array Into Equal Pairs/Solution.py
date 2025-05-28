class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_count = {}
        for i in range(len(nums)):
            if nums[i] in num_count:
                num_count[nums[i]] += 1
            else:
                num_count[nums[i]] = 1

        if int(len(nums)) % 2 != 0:
            return(False)
        else:
            return(all(value % 2 == 0 for value in num_count.values()))