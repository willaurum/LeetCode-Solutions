
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums = [0,1,2,2,3,0,4,2]
        # val = 2
        #               Output: 5, nums = [0,1,4,0,3,_,_,_]
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
                continue
            else:
                nums.insert(0, nums.pop(i))

        return(abs(k-len(nums)))