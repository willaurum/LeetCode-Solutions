class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        prev = nums[0]

        while right < len(nums):

            while right < len(nums) and nums[right] == prev:
                right += 1

            nums[left] = nums[right-1]
            left += 1
            if right < len(nums):
                prev = nums[right]


        return left