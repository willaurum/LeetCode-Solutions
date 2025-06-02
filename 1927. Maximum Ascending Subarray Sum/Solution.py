class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        chk = 0
        chk += nums[0]
        ans += nums[0]
        for i in range(1, len(nums)):
            
            if nums[i] > nums[i - 1]:
                chk += nums[i]
            else:
                chk = nums[i]
            ans = max(ans, chk)

        return(ans)