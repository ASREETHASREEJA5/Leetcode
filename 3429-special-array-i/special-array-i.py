class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return True
        i = 0
        while(i<len(nums)-1):
            if nums[i]%2 == 0 and nums[i+1]%2 != 0:
                i+=1
            elif nums[i+1]%2 == 0 and nums[i]%2 != 0:
                i+=1
            else:
                return False
        return True

        