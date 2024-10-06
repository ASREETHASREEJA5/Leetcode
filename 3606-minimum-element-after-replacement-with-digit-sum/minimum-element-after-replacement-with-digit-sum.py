class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum1 =0 
            n = nums[i]
            while n>0:
                rem = n%10
                sum1+=rem
                n//=10
            nums[i]=sum1
        return min(nums) 
        