class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        for i in range(len(nums)):
            if i>max_ind:
                return False
            max_ind = max(max_ind,i+nums[i])
        return True


        