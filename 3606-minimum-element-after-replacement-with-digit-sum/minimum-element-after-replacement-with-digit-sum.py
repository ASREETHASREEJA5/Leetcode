class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            sum1 =0 
            n = nums[i]
            while n>0:
                rem = n%10
                sum1+=rem
                n//=10
            if ans>sum1:
                ans = sum1
        return ans 
        